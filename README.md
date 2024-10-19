[시스템 구조 요약] - MQTT 프로토콜

- **드론**에서 **MAVLink 메시지**를 사용해 **Mobius Broker 서버**로 데이터를 전송.
- **Mobius Broker** 서버에서 데이터를 받아 json으로 파싱 후, **내장된 MySQL** 데이터베이스에 저장.
- **Flask 경로 탐색 서버**는 **Mobius Broker 내장 MySQL의** 데이터를 이용해 경로를 계산하고, MAVLink 메시지로 json 데이터를 파싱 후 드론에게 전송.

(위도와 경도 데이터는 따로 변수를 선언해 받은 다음, DB를 거치지 않고 실시간으로 직접 Flask 서버에 쏜다)

## Mobius-Broker 서버 역할
1. SITL 연결: 다수의 실제 드론으로 테스트하는 것은 효율적이지 못하므로, SITL(드론 시뮬레이션)을 이용한다. (SITL이 MQTT 프로토콜을 이용하여 가상의 드론 데이터를 MAVLink 메시지 형태로 Mobius-Broker에 전송)
2. MAVLink 메시지 수신 및 json 데이터로 파싱: 드론(SITL)으로부터 온 MAVLink 메시지를 수신하고, 이를 JSON으로 변환한 후 MySQL 데이터베이스에 저장하거나 필요한 처리를 한다.
3. Flask 서버와의 통신: Flask 서버는 필요할 때 Mobius-Broker에서 데이터를 조회하거나, 경로를 계산해 결과를 다시 드론에게 전달한다.
(Mobius-Broker는 주로 데이터 브로커 역할을 수행하며, 특정한 비즈니스 로직(API)를 제공하는 주체는 x)

## Flask 서버 역할: json → MAVLink 메시지(이진 형태) 파싱 필요
1. 경로 계산 요청 처리: Flask 서버는 드론의 경로를 계산하는 로직을 처리하며, 필요한 데이터를 Mobius의 MySQL 데이터베이스에서 조회할 수 있다.
2. json 데이터 수신 및 MAVLink 메시지로 파싱: Mobius-Broker로부터 온 json 데이터를 이용하며, 드론에게 데이터 전송 시 MAVLink 메시지로 파싱한다.
(Flask 서버에서 REST API를 정의하여, 경로 계산 및 데이터 요청을 처리)

<img src="https://github.com/user-attachments/assets/3b7c555c-82c0-497f-b261-5b07695e1f70" width="800" height="400"/>
