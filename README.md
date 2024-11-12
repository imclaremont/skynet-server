## 전체 시스템 구조도
<img src="https://github.com/user-attachments/assets/77439eac-6737-4c6f-8770-8e43c1038651" width="700"/>

## OneDrone -> Mobius -> Flask
* OneDrone to Mobius topic: /Mobius/[GCS이름]/Drone_Data/[드론이름]/[sortie이름]/orig
* Mobius to Flask topic: drone/status
  
<b>OneDrone으로부터 구독한 MAVLink 바이너리 메시지를 Mobius에서 JSON으로 변환해 Flask로 발행</b>

## Flask -> Mobius -> OneDrone
* Flask to Mobius topic: drone/commands
* Mobius to OneDrone topic: 미정
  
<b>Flask로부터 구독한 MAVLink 바이너리 메시지와 JSON을 Mobius에서 그대로 OneDrone으로 발행</b>

① ARM, SET_MODE: MAVLink 바이너리 메시지 타입

② 나머지 데이터들(미션 명령): JSON 타입
