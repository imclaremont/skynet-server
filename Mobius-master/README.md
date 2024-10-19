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
1. pxy_ws.js 내용과 동일 (CSE 비활성화)

2. MAVLink 메시지를 json 데이터 형식으로 파싱: mqtt_message_handler() 함수 + mavlinkToJSON() 함수

추출할 데이터 4가지

드론의 경도/위도, 배터리 잔량, 드론 ID, mission_item(현재 가고 있는 목표지점을 알 수 있는지 확인하는 용도)  

3. Flask 서버로 전송: mqtt.connect() 부분의 'mqtt://flask_server_ip'에는 실제 Flask 서버의 IP 주소를 입력

### ㅇMQTT 라이브러리 - 발행(publish) 역할

설치 명령어: % npm install mqtt

import문: const mqtt = require('mqtt');

### ㅇpymavlink 라이브러리 - MAVLink 메시지의 각 필드를 추출

설치 명령어: % npm install mavlink

import문: const { MAVLink } = require('mavlink');

### ㅇjson 라이브러리 - 추출한 필드를 JSON 형식으로 변환

JavaScript 내장 라이브러리 (별도의 설치나 import 불필요)

---------------------------------------------------

## [MQTT 브로커(mosquitto 서버) 구독 테스트 터미널 명령]
mosquitto_sub -h localhost -t /mytopic/1

## [MQTT 브로커(mosquitto 서버) 발행 테스트 터미널 명령]
mosquitto_pub -h localhost -t /mytopic/1 -m "Hello MQTT test"

---------------------------------------------------

## SITL 연결 (w/한신님)
