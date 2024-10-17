[시스템 구조 요약] - MQTT 프로토콜

- **드론**에서 **MAVLink 메시지**를 사용해 **Mobius Broker 서버**로 데이터를 전송.
- **Mobius Broker** 서버에서 데이터를 받아 json으로 파싱 후, **내장된 MySQL** 데이터베이스에 저장.
- **Flask 경로 탐색 서버**는 **Mobius Broker 내장 MySQL의** 데이터를 이용해 경로를 계산하고, MAVLink 메시지로 json 데이터를 파싱 후 드론에게 전송.

(위도와 경도 데이터는 따로 변수를 선언해 받은 다음, DB를 거치지 않고 실시간으로 직접 Flask 서버에 쏜다)


Mobius-Broker 서버 측) MAVLink 메시지(이진 형태) → json 파싱 필요

Flask 서버 측) json → MAVLink 메시지(이진 형태) 파싱 필요
