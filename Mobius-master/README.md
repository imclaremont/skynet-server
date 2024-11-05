## mobius.js (mobius 서버 실행 명령어: node mobius.js)
your_MySQL_password에 본인의 MySQL pwd로 수정 필요

※ sitl 없이 mobius 서버와 flask 서버 간의 통신 테스트 코드 맨 아래에 주석처리 해두었습니다. 필요하시다면 사용하세요!

## app.js (main 역할을 수행하는 파일)
모든 RESTful method에 비어있었던 경로값을 '/default'로 설정 

app.post('/default', onem2mParser, (request, response) => {

app.get('/default', onem2mParser, (request, response) => {

app.put('/default', onem2mParser, (request, response) => {

app.delete('/default', onem2mParser, (request, response) => {

## pxy_ws.js (WebSocket 프록시 파일)
node mobius.js 로 서버 실행 시, "Target CSE(localhost) is not ready" 문구가 뜨는 문제 발생

CSE를 사용하지 않으므로 해당 부분 코드 주석으로 비활성화 처리로 해결

## pxy_mqtt.js (MQTT 프록시 파일)
### 1. pxy_ws.js 내용과 동일 (CSE 비활성화)

### 2. Flask 서버 포트 설정 (mqtt 라이브러리 사용)
pxymqtt_client = mqtt.connect('mqtt://127.0.0.1:<b>1884</b>') 부분 필요 시 수정 필요 ('mqtt://MQTT_BROKER_IP:<b>MQTT_PORT_NUMBER</b>')

### 3. Flask 서버로부터 온 JSON 데이터 처리 로직: 2번의 Flask 서버 포트 설정 부분과 4번의 mqtt_message_handler() 함수 부분 사이에 작성

### 4. OneDrone으로부터 온 JSON 데이터 처리 로직: mqtt_message_handler() 함수

### [추출할 데이터 4가지]

#### ① 드론 ID 및 상태(ARMED or DISARMED, GUIDED) - MQTT topic: 'drone/status'

필드명: system_id, armed, guided, timestamp(미정)

#### ② 경도/위도 및 고도(절대고도 = 해발고도) - MQTT topic: 'drone/position'

필드명: latitude, longitude, altitude, timestamp(미정)

#### ③ 배터리 잔량 - MQTT topic: 'drone/battery_status'

필드명: battery_remaining, timestamp(미정)

#### ④ mission_item(현재 가고 있는 목표지점을 알 수 있는지 확인하는 용도) - MQTT topic: 'drone/mission_status'

필드명: mission_sequence, timestamp(미정)

---------------------------------------------------

## [MQTT 브로커(mosquitto 서버) 구독 테스트 터미널 명령]
mosquitto_sub -h localhost -t /mytopic/1

## [MQTT 브로커(mosquitto 서버) 발행 테스트 터미널 명령]
mosquitto_pub -h localhost -t /mytopic/1 -m "Hello MQTT test"

---------------------------------------------------

## OneDrone 연결
포트번호: 1883

---------------------------------------------------


## (참고) Mobius-Broker SW Architecture
<div align="center">
<img src="https://user-images.githubusercontent.com/29790334/28245393-a1159d5e-6a40-11e7-8948-4262bf29c371.png" width="500"/>
</div>
