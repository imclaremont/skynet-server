## 전체 시스템 구조도
<img src="https://github.com/user-attachments/assets/77439eac-6737-4c6f-8770-8e43c1038651" width="700"/>

## 전체 시스템 흐름
* 드론(SITL): 드론의 상태를 MAVLink 메시지 데이터 타입으로 OneDrone에 전송
* OneDrone: MAVLink 메시지를 수신하고, 이를 JSON 형식으로 변환한 후 MQTT 메시지로 Mobius 서버에 발행
* Mobius 서버: OneDrone으로부터 수신한 데이터 중 필요한 데이터를 추출해 Flask 서버에 JSON 데이터 형식으로 발행, 필요한 경우에는 MySQL에 저장
* Flask 서버: Mobius로부터 수신한 데이터를 경로 탐색 알고리즘에 사용하고, 드론(SITL)에 명령

1. OneDrone -> Mobius -> Flask
* OneDrone to Mobius topic: /Mobius/[GCS이름]/Drone_Data/[드론이름]/[sortie이름]/orig
* Mobius to Flask topic: drone/status
OneDrone으로부터 온 MAVLink 바이너리 메시지를 Mobius에서 필드값추출 없이 JSON으로만 변환해 Flask로 쏴주는 형태

2. Flask -> Mobius -> OneDrone
* Flask to Mobius topic: drone/commands
* Mobius to OneDrone topic: 미정
Flask로부터 온 데이터들을 Mobius에서 아래와 같이 처리 후 OneDrone으로 발행
① ARM, SET_MODE: MAVLink 바이너리 메시지 타입으로 Mobius에 오고 OneDrone으로 그대로 발행
② 나머지 데이터들(미션 명령): JSON 타입으로 Mobius에 오고 OneDrone으로 그대로 발행
