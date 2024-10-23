## 1. paho-mqtt 라이브러리 사용 - MQTT 프로토콜에서 Flask 서버가 구독자(subscriber) 역할을 수행

### flask_server.py
- Flask 서버로, MQTT 브로커로부터 수신한 메시지를 처리, 기상 정보 획득

### mqtt_client.py
- MQTT 클라이언트로서 특정 토픽을 구독하고, 데이터를 수신하여 처리

#### 임시: MQTT topic을 'drone/request' 하나로 drone 데이터를 처리.

 
### weather_api.py
- 기상청 API를 이용해 현재 시각을 기준으로 기상 정보를 수신하고, 드론 운행에 필요한 데이터를 처리


## 2. json 라이브러리 사용 - json 형식의 데이터로부터 드론에게 전송할 데이터 필드를 추출 + MAVLink의 형식에 맞게 스케일을 변환

## 2. pymavlink 라이브러리 사용 - 추출한 데이터를 MAVLink 메시지로 변환 후 드론에게 전송

## + MAVLink 메시지를 드론에게 전송한 후, 드론으로부터 오는 응답 처리
드론이 경로를 수신하고 명령을 수행했는지 확인하기 위해 `ACK` or 상태 메시지를 받을 수 있도록 구성
