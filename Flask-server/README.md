## 1. paho-mqtt 라이브러리 사용 - MQTT 프로토콜에서 Flask 서버가 구독자(subscriber) 역할을 수행

### flask_server.py
- Flask 서버로, MQTT 브로커로부터 수신한 메시지를 처리, 기상 정보 획득

#### '/drones', methods=['GET'] : 현재 드론 상태를 JSON 형태로 반환하는 임시 엔드포인트

### mqtt_client.py
- MQTT 클라이언트로서 특정 토픽을 구독하고, 데이터를 수신하여 처리

#### ① 드론 ID 및 상태(ARMED or DISARMED, GUIDED) - MQTT topic: 'drone/status'
#### ② 경도/위도 및 고도(절대고도 = 해발고도) - MQTT topic: 'drone/position'
#### ③ 배터리 잔량 - MQTT topic: 'drone/battery_status'
#### ④ mission_item(현재 가고 있는 목표지점을 알 수 있는지 확인하는 용도) - MQTT topic: 'drone/mission_status'
 
### weather_api.py
- 기상청 API를 이용해 현재 시각을 기준으로 기상 정보를 수신하고, 드론 운행에 필요한 데이터를 처리


## 2. json 라이브러리 사용 - json 형식의 데이터로부터 드론에게 전송할 데이터 필드를 추출 + MAVLink의 형식에 맞게 스케일을 변환

## 2. pymavlink 라이브러리 사용 - 추출한 데이터를 MAVLink 메시지로 변환 후 드론에게 전송

## + MAVLink 메시지를 드론에게 전송한 후, 드론으로부터 오는 응답 처리
드론이 경로를 수신하고 명령을 수행했는지 확인하기 위해 `ACK` or 상태 메시지를 받을 수 있도록 구성

--------------------------------------------------------------------------------

## 라이브러리 설치
pip install paho-mqtt

pip install pymavlink

pip install requests

pip install python-dotenv
