# mqtt_client.py

import paho.mqtt.client as mqtt
from pymavlink import mavutil
import drone
import json

# MQTT 브로커 정보
MQTT_BROKER = '127.0.0.1'
TOPICS = [
    'drone/status',
    'drone/position',
    'drone/battery_status',
    'drone/mission_status'
]

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

# 드론과 MAVLink 연결 (시뮬레이터 또는 실제 드론)
mavlink_connection = mavutil.mavlink_connection('udp:127.0.0.1:14550')

# MQTT 클라이언트 설정
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)


# 연결 시 호출되는 콜백 함수
def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        print("\n\nSuccess Connect!\n\n")
        for topic in TOPICS:
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

# (임시)드론 상태를 전송하는 함수 - 드론 상태를 gcs에 전송, 정확한 프로토콜을 알지 못해서 일단 mqtt로 가정.
# def send_drone_status():
#     while True:
#         # MAVLink 메시지 수신
#         msg = mavlink_connection.recv_match(blocking=True)
#         if msg:
#             # 메시지 종류에 따라 처리
#             if msg.get_type() == 'GLOBAL_POSITION_INT':
#                 lat = msg.lat / 1e7
#                 lon = msg.lon / 1e7
#                 alt = msg.alt / 1000.0

#                 # 드론 위치 및 상태 정보 MQTT 메시지 생성
#                 status_message = {
#                     "location": {
#                         "lat": lat,
#                         "lon": lon,
#                         "alt": alt
#                     }
#                 }

#                 # MQTT 메시지로 전송
#                 client.publish(TOPIC_RESPONSE, json.dumps(status_message))

#             # 배터리 상태 수신
#             elif msg.get_type() == 'SYS_STATUS':
#                 battery_voltage = msg.voltage_battery / 1000.0
#                 battery_current = msg.current_battery / 100.0
#                 battery_remaining = msg.battery_remaining

#                 # 배터리 상태 MQTT 메시지 생성
#                 status_message = {
#                     "battery": {
#                         "voltage": battery_voltage,
#                         "current": battery_current,
#                         "remaining": battery_remaining
#                     }
#                 }

#                 # MQTT 메시지로 전송
#                 client.publish(TOPIC_RESPONSE, json.dumps(status_message))

#         time.sleep(1)  # 주기적으로 상태 전송


#MQTT 클라이언트를 시작
def start_mqtt_client():
    print("\n\nStart MQTT Client\n\n")
    client.on_connect = on_connect
    client.on_message = on_message  
    client.connect(MQTT_BROKER)
    client.loop_start()
    

# MAVLink 통신을 대기 (필요 시 추가 로직 포함 가능)
# mavlink_connection.wait_heartbeat()
# print("Heartbeat from system (system %u component %u)" % (mavlink_connection.target_system, mavlink_connection.target_component))
