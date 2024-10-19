## 사용 라이브러리
1. pymavlink 라이브러리 - MAVLink 메시지의 각 필드를 추출
2. json 라이브러리 - 추출한 필드를 JSON 형식으로 변환

## mobius.js (mobius 서버 실행 파일)
% node mobius.js

## app.js (main 역할을 수행하는 파일)
모든 RESTful method에 비어있었던 경로값을 '/default'로 설정 


app.post('/default', onem2mParser, (request, response) => {

app.get('/default', onem2mParser, (request, response) => {

app.put('/default', onem2mParser, (request, response) => {

app.delete('/default', onem2mParser, (request, response) => {

## pxy_ws.js
node mobius.js 로 서버 실행 시에 Target CSE(localhost) is not ready 가 뜨는 문제 발생

CSE를 사용하지 않으므로 해당 부분 코드 주석으로 비활성화 처리로 해결

## pxy_mqtt.js
1. pxy_ws.js 내용과 동일 (CSE 비활성화)

2. MAVLink 메시지를 json 데이터 형식으로 파싱하고, Flask 서버로 전송하는 로직 구현 (mqtt_message_handler 함수)

## MQTT 브로커(mosquitto 서버) 구독 테스트 터미널 명령
mosquitto_sub -h localhost -t /mytopic/1

## MQTT 브로커(mosquitto 서버) 발행 테스트 터미널 명령
mosquitto_pub -h localhost -t /mytopic/1 -m "Hello MQTT test"

## Mobius-Broker SW Architecture
<div align="center">
<img src="https://user-images.githubusercontent.com/29790334/28245393-a1159d5e-6a40-11e7-8948-4262bf29c371.png" width="500"/>
</div>

## SITL 연결
------------
