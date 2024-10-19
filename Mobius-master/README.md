


app.js 수정

드론으로부터 오는 MAVLink 메시지를 json으로 파싱하고, Flask 서버로 전송하는 코드는 pxy_mqtt.js 파일에 작성 예정

1. pymavlink 라이브러리 사용 - MAVLink 메시지의 각 필드를 추출
2. json 라이브러리 사용 - 추출한 필드를 JSON 형식으로 변환

## MQTT 브로커(mosquitto 서버) 구독 테스트 터미널 명령
mosquitto_sub -h localhost -t /mytopic/1

## MQTT 브로커(mosquitto 서버) 발행 테스트 터미널 명령
mosquitto_pub -h localhost -t /mytopic/1 -m "Hello MQTT test"

## Mobius-Broker SW Architecture
<div align="center">
<img src="https://user-images.githubusercontent.com/29790334/28245393-a1159d5e-6a40-11e7-8948-4262bf29c371.png" width="500"/>
</div>

## SITL 연결

## mobius 서버 실행 터미널 명령어
node mobius.js
