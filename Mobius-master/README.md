## mobius.js (mobius 서버 실행 파일)
% node mobius.js

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

### 2. MAVLink 메시지 -> JSON 파싱: mqtt_message_handler() 함수

### [추출할 데이터 4가지]
https://claremont.tistory.com/entry/MAVLink-%EB%A9%94%EC%8B%9C%EC%A7%80-%E2%86%92-JSON-%ED%8C%8C%EC%8B%B1-%ED%9B%84-Flask-%EC%84%9C%EB%B2%84-%EC%A0%84%EC%86%A1-%EC%98%88%EC%8B%9C-%EC%BD%94%EB%93%9C

#### ① 드론 ID 및 상태(ARMED or DISARMED, GUIDED) - MQTT topic: 'drone/status'
#### ② 경도/위도 및 고도(절대고도/해발고도) - MQTT topic: 'drone/position'
#### ③ 배터리 잔량 - MQTT topic: 'drone/battery_status'
#### ④ mission_item(현재 가고 있는 목표지점을 알 수 있는지 확인하는 용도) - MQTT topic: 'drone/mission_status'

### 3. Flask 서버로 전송: mqtt.connect() 부분의 'mqtt://flask_server_ip'에는 실제 Flask 서버의 IP 주소를 입력

###  (참고) pxy_mqtt.js 파일에서 사용하는 라이브러리 3가지
https://claremont.tistory.com/entry/Nodejs-MQTT-PyMAVLink-JSON-%EB%9D%BC%EC%9D%B4%EB%B8%8C%EB%9F%AC%EB%A6%AC
#### ① MQTT 라이브러리
#### ② pymavlink 라이브러리
#### ③ json 라이브러리

## [MQTT 브로커(mosquitto 서버) 구독 테스트 터미널 명령]
mosquitto_sub -h localhost -t /mytopic/1

## [MQTT 브로커(mosquitto 서버) 발행 테스트 터미널 명령]
mosquitto_pub -h localhost -t /mytopic/1 -m "Hello MQTT test"

---------------------------------------------------

## SITL 연결 (w/한신님)
진행 예정
