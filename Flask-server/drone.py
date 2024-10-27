# drone.py : 임의로 정의한 드론 상태 정보

drone_statuses = {}

#드론 클래스 정의
class Drone:
    def __init__(self, drone_id, isArmed, isGuided, latitude, longitude, altitude, battery_status, mission_status):
        self.id = drone_id
        self.isArmed = isArmed
        self.isGuided = isGuided
        self.latitude = latitude
        self.longitude = longitude
        self.altitude = altitude
        self.battery_status = battery_status
        self.mission_status = mission_status

    def __repr__(self):
        return f"Drone(id={self.id}, position={self.position}, battery={self.battery_status})"

#### ① 드론 ID 및 상태(ARMED or DISARMED, GUIDED) - MQTT topic: 'drone/status'
#### ② 경도/위도 및 고도(절대고도 = 해발고도) - MQTT topic: 'drone/position'
#### ③ 배터리 잔량 - MQTT topic: 'drone/battery_status'
#### ④ mission_item(현재 가고 있는 목표지점을 알 수 있는지 확인하는 용도) - MQTT topic: 'drone/mission_status'

#전역 드론 상태 딕셔너리에 드론 상태 업데이트
def update_drone_status(drone):
    drone_statuses[drone.id] = {
        "isArmed": drone.isArmed,
        "isGuided": drone.isGuided,
        "latitude": drone.latitude,
        "longitude": drone.longitude,
        "altitude": drone.altitude,
        "battery": drone.battery_status,
        "mission_status": drone.mission_status
    }

#현재 드론 상태 정보를 반환
def get_drone_status(): 
    return drone_statuses
