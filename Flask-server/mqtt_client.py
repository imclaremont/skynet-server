# mqtt_client.py

import paho.mqtt.client as mqtt
import drone
import json

from pymavlink.dialects.v20 import common as mavlink2
from pymavlink import mavutil

# MQTT 브로커 정보
MQTT_BROKER = '127.0.0.1'
# SUB_TOPICS = [
#     'drone/status',
#     'drone/position',
#     'drone/battery_status',
#     'drone/mission_status'
# ]
SUB_TOPIC = 'drone/status'
PUB_TOPIC = 'drone/commands'

# 기본값 설정
drone_info = {
    'drone_id': None,
    'isArmed': None,
    'isGuided': None,
    'latitude': None,
    'longitude': None,
    'altitude': None,
    'battery_status': None,
    'mission_status': None
}

# MQTT 클라이언트 설정
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

# 연결 시 호출되는 콜백 함수
def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        print("\n\nSuccess Connect!\n\n")
        for topic in SUB_TOPICS:
            client.subscribe(topic)  # 각 토픽을 구독합니다.

    if reason_code > 0:
        print(f'\n\nConnected with result code {reason_code}\n\n')


# 메시지를 수신할 때 호출되는 콜백 함수 수정
def on_message(client, userdata, message):
    topic = message.topic  # 수신된 메시지의 토픽
    payload = str(message.payload.decode("utf-8"))

    print(f"\nReceived message on topic '{topic}': {payload}\n")
    
    # 각 토픽에 따라 get_drone_status 호출
    get_drone_status(topic, payload)


# 수신받은 드론 정보를 저장
def get_drone_status(topic, payload):
    data = json.loads(payload)  # JSON 형식으로 파싱


    # 토픽에 따라 정보 저장
    if topic == 'drone/status':
        drone_info['drone_id'] = data['system_id']
        drone_info['isArmed'] = data['armed']
        drone_info['isGuided'] = data['guided']

    elif topic == 'drone/position':
        drone_info['latitude'] = data['latitude']
        drone_info['longitude'] = data['longitude']
        drone_info['altitude'] = data['altitude']


    elif topic == 'drone/battery_status':
        drone_info['battery_status'] = data['battery_remaining']

    elif topic == 'drone/mission_status':
        drone_info['mission_status'] = data['mission_sequence']


    # 모든 정보가 수집된 경우에만 드론 객체 생성
    if all(value is not None for value in drone_info.values()):
        drone_obj = drone.Drone(
            drone_info['drone_id'],
            drone_info['isArmed'],
            drone_info['isGuided'],
            drone_info['latitude'],
            drone_info['longitude'],
            drone_info['altitude'],
            drone_info['battery_status'],
            drone_info['mission_status']
        )
        print(f"\nCall update_drone\n")
        drone.update_drone_status(drone_obj)
                
        # 드론 정보 초기화
        reset_drone_info()

def reset_drone_info():
    global drone_info
    drone_info = {
        'drone_id': None,
        'isArmed': None,
        'isGuided': None,
        'latitude': None,
        'longitude': None,
        'altitude': None,
        'battery_status': None,
        'mission_status': None
    }


# MAVLink 메시지 디코딩 함수
def decode_mavlink_message(mav_msg_byte):

    mav = mavlink2.MAVLink(None)  # 연결 없이 MAVLink 객체 생성
    try:
        # 메시지 파싱
        msg = mav.decode(mav_msg_byte)
        return msg
    except Exception as e:
        return f"Failed to decode message: {e}"


# 제어 명령을 발행하는 함수
def publish_control_command(command_data):
    command = command_data.get("command")
    mav_msg = None

    print(f"\ncommand : {command}\n")


    if command == "SET_MODE":
        # SET MODE 명령
        mode = command_data.get("mode")
        sys_id = command_data.get("sys_id")
        mode_id = mavutil.mavlink.MAV_MODE_GUIDED_ARMED if mode == "GUIDED" else mavutil.mavlink.MAV_MODE_MANUAL_ARMED

        mav_msg = mavlink2.MAVLink(None).set_mode_encode(
            target_system = sys_id,  # 대상 시스템 ID
            base_mode = mode_id,
            custom_mode = 0
        )


    elif command == "ARM":
        # ARM 명령
        sys_id = command_data.get("sys_id")
        comp_id = command_data.get("comp_id")

        mav_msg = mavutil.mavlink.MAVLink_command_long_message(
            target_system = sys_id,             # 시스템 ID (드론의 고유 식별자)
            target_component = comp_id,         # 컴포넌트 ID
            command=mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,   # 명령: ARM
            confirmation=0,
            param1=1,  # 1은 ARM, 0은 DISARM
            param2=0, param3=0, param4=0, param5=0, param6=0, param7=0
        )

    elif command == "TAKEOFF":
        # TAKEOFF 명령
        sys_id = command_data.get("sys_id")
        comp_id = command_data.get("comp_id")
        altitude = command_data.get("altitude", 10)  # 기본 이륙 고도

        mav_msg = mavutil.mavlink.MAVLink_command_long_message(
            target_system=sys_id,
            target_component=comp_id,
            command=mavutil.mavlink.MAV_CMD_NAV_TAKEOFF,
            confirmation=0,
            param1=0, param2=0, param3=0, param4=0,
            param5=0, param6=0,  # 위도/경도는 생략
            param7=altitude  # 목표 고도
        )

    elif command == "MOVE_TO":
        # 특정 위치로 이동하는 MOVE_TO 명령
        sys_id = command_data.get("sys_id")
        comp_id = command_data.get("comp_id")

        mav_msg = mavutil.mavlink.MAVLink_set_position_target_global_int_message(
            0,  # time_boot_ms (ignored)
            sys_id,
            comp_id,
            mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT_INT,  # frame
            0b0000111111111000,  # type_mask (only positions enabled)
            int(command_data['latitude'] * 1e7),  # 위도
            int(command_data['longitude'] * 1e7),  # 경도
            command_data['altitude'],  # 고도
            0, 0, 0,  # x, y, z velocity (not used)
            0, 0, 0,  # x, y, z acceleration (not used)
            0, 0  # yaw, yaw_rate (not used)
        )

    elif command == "LAND":
        # LAND 명령
        sys_id = command_data.get("sys_id")
        comp_id = command_data.get("comp_id")

        mav_msg = mavutil.mavlink.MAVLink_command_long_message(
            target_system=sys_id,
            target_component=comp_id,
            command=mavutil.mavlink.MAV_CMD_NAV_LAND,
            confirmation=0,
            param1=0, param2=0, param3=0, param4=0,
            param5=0, param6=0, param7=0
        )

    print(f"\nmav_msg : \n{mav_msg}")

    if mav_msg:
        mavlink_msg_bytes = mav_msg.pack(mavutil.mavlink.MAVLink('', 2, 1))
        client.publish(PUB_TOPIC, mavlink_msg_bytes)

        # # 비트 문자열 변환
        # mavlink_message_bits = ''.join(format(byte, '08b') for byte in mavlink_msg_bytes)

        # # 4비트 단위 띄어쓰기
        # formatted_bits = ' '.join(mavlink_message_bits[i:i+4] for i in range(0, len(mavlink_message_bits), 4))
        # print("\nFormatted bits:", formatted_bits)

        # 디코딩
        # decoded_msg = decode_mavlink_message(bytearray(mavlink_msg_bytes))
        # print("\nDecoded message:", decoded_msg)

        print(f"\nPublished MAVLink command to {PUB_TOPIC}: {mavlink_msg_bytes}")
    else:
        print(f"\nUnknown command: {command}")



#MQTT 클라이언트를 시작
def start_mqtt_client():
    print("\n\nStart MQTT Client\n\n")
    client.on_connect = on_connect
    client.on_message = on_message  
    client.connect(MQTT_BROKER, port=1884)
    client.loop_start()
    
