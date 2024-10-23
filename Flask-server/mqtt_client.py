# mqtt_client.py

import paho.mqtt.client as mqtt
from pymavlink import mavutil
import drone

# MQTT 브로커 정보
MQTT_BROKER = '127.0.0.1'
TOPIC_REQUEST = 'drone/request'
TOPIC_RESPONSE = 'drone/response'

# 드론과 MAVLink 연결 (시뮬레이터 또는 실제 드론)
mavlink_connection = mavutil.mavlink_connection('udp:127.0.0.1:14550')

# MQTT 클라이언트 설정
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

# 연결 시 호출되는 콜백 함수
def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        print("\n\nSuccess Connect!\n\n")
        client.subscribe(TOPIC_REQUEST)

    if reason_code > 0:
        print(f'\n\nConnected with result code {reason_code}\n\n')

#메시지를 수신할 때 호출되는 콜백 함수
def on_message(client, userdata, message):
        print("received message: ", str(message.payload.decode("utf-8")))
        get_drone_status(message)

# 수신받은 드론 정보를 저장
def get_drone_status(message):
     
     # message를 drone_id, position 등으로 분류 로직

    # 저장
     drone(message)

# (임시)드론 상태를 전송하는 함수 - 드론 상태를 gcs에 전송 정확한 프로토콜을 알지 못해서 일단 mqtt로 가정.
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
