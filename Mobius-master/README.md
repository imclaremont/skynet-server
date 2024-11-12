## mobius.js (mobius 서버 실행 명령어: node mobius.js)
your_MySQL_password에 본인의 MySQL pwd로 수정 필요

## app.js (main 역할을 수행하는 파일)
모든 RESTful method에 비어있었던 경로값을 '/default'로 설정 

* app.post('/default', onem2mParser, (request, response) => {

* app.get('/default', onem2mParser, (request, response) => {

* app.put('/default', onem2mParser, (request, response) => {

* app.delete('/default', onem2mParser, (request, response) => {

## pxy_ws.js (WebSocket 프록시 파일)
node mobius.js 로 서버 실행 시, "Target CSE(localhost) is not ready" 문구가 뜨는 문제 발생

CSE를 사용하지 않으므로 해당 부분 코드 주석으로 비활성화 처리

## pxy_mqtt.js (MQTT 프록시 파일)
* pxy_ws.js 내용과 동일 (CSE 비활성화)

* mqtt_message_handler() 함수에 모든 처리 로직 구현

flask_client = mqtt.connect('mqtt://127.0.0.1:1884') 부분 추후 수정 필요 MQTT_BROKER_IP:MQTT_PORT_NUMBER

## OneDrone 연결
포트번호: 1883 (MQTT 기본 비보안 포트)

---------------------------------------------------

## (참고) [MQTT 브로커(mosquitto 서버) 구독 테스트 터미널 명령어]
* 구독(subscribe): mosquitto_sub -h localhost -t /mytopic/1

* 발행(publish): mosquitto_pub -h localhost -t /mytopic/1 -m "Hello MQTT test"

---------------------------------------------------

## (참고) Mobius-Broker SW Architecture
<div align="center">
<img src="https://user-images.githubusercontent.com/29790334/28245393-a1159d5e-6a40-11e7-8948-4262bf29c371.png" width="500"/>
</div>
