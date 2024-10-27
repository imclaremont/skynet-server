# flask_server.py

import mysql.connector
from flask import Flask,render_template, jsonify, request
from drone import get_drone_status
import threading
import mqtt_client, weather_api
from dotenv import load_dotenv
import os

load_dotenv()

db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')

app = Flask(__name__)

# 종료 이벤트
shutdown_event = threading.Event()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pathfinding', methods=['POST'])
def pathfinding():
    sname = request.form['sname']
    dname = request.form['dname']

    # 경로 계산 로직
    route = f"출발지 : {sname}, 목적지 : {dname}의 경로 계산 완료!"
    print(route)


    # 경로 전달


    return request.json


# 임시 현재 드론 상태를 반환하는 엔드포인트
@app.route('/drones', methods=['GET'])
def get_drones():
    drones = get_drone_status()  # 드론 상태를 가져옴

    print(f"\n{drones}\n")
    return jsonify(drones)

#Flask 서버를 실행
def run_flask():
    app.run(host='127.0.0.1', port=5000)
    

if __name__ == '__main__':
    # MQTT 클라이언트를 별도의 스레드에서 실행
    mqtt_thread = threading.Thread(target=mqtt_client.start_mqtt_client)
    mqtt_thread.start()

    # Flask 서버 실행
    try:
        run_flask()
        
    except KeyboardInterrupt:
        print("Flask server shutting down...")
        shutdown_event.set()  # 종료 이벤트 설정
        mqtt_client.client.loop_stop()  # MQTT 클라이언트 정지