드론으로부터 오는 MAVLink 메시지를 json으로 파싱하고, Flask 서버로 전송하는 코드는 pxy_mqtt.js 파일에 작성 예정

1. pymavlink 라이브러리 사용 - MAVLink 메시지의 각 필드를 추출
2. json 라이브러리 사용 - 추출한 필드를 JSON 형식으로 변환

## Mobius-Broker SW Architecture
<div align="center">
<img src="https://user-images.githubusercontent.com/29790334/28245393-a1159d5e-6a40-11e7-8948-4262bf29c371.png" width="500"/>
</div>

<img src="https://github.com/user-attachments/assets/49a2f024-1e4e-4b19-8579-2e65380fa9a7" width="200" height="200"/>
<img src="https://github.com/user-attachments/assets/59ca51a8-9a2f-4707-9bef-42431265e9d4" width="250" height="200"/>

## ERD
<img src="https://github.com/user-attachments/assets/afd58f80-bf7b-4f7c-bb17-fde8eb431d20" width="1800" height="600"/>
