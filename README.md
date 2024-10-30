# 시나리오
## [프로토콜] SITL과 OneDrone: UDP, 나머지 전부: MQTT
* SITL(ArduPilot): 드론의 상태를 MAVLink 메시지 데이터 타입으로 OneDrone에 전송
* OneDrone: MAVLink 메시지를 수신하고, 이를 JSON 형식으로 변환한 후 MQTT 메시지로 mobius 서버에 발행
* mobius 서버: OneDrone으로부터 수신한 데이터 중 필요한 데이터를 추출해 flask 서버에 JSON 데이터 형식으로 발행, 필요한 경우에는 MySQL에 저장
* flask 서버: mobius로부터 수신한 데이터를 경로 탐색 알고리즘에 사용하고, SITL(ArduPilot)에 명령

## (참고) Mobius-Broker SW Architecture
<div align="center">
<img src="https://user-images.githubusercontent.com/29790334/28245393-a1159d5e-6a40-11e7-8948-4262bf29c371.png" width="500"/>
</div>
