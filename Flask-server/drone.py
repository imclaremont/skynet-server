# drone.py : 임의로 정의한 드론 상태 정보

drone_statuses = {}

#드론 클래스 정의
class Drone:
    def __init__(self, drone_id, isArmed, isGuided, latitude, longitude, altitude, velocity, battery_status, mission_status):
        self.id = drone_id
        self.isArmed = isArmed
        self.isGuided = isGuided
        self.latitude = latitude
        self.longitude = longitude
        self.altitude = altitude
        self.velocity = velocity    # [vx, vy, vz]
        self.battery_status = battery_status
        self.mission_status = mission_status

    def __repr__(self):
        return f"Drone(id={self.id}, position={self.position}, battery={self.battery_status})"


#전역 드론 상태 딕셔너리에 드론 상태 업데이트
def update_drone_status(drone):
    drone_statuses[drone.id] = {
        "isArmed": drone.isArmed,
        "isGuided": drone.isGuided,
        "latitude": drone.latitude,
        "longitude": drone.longitude,
        "altitude": drone.altitude,
        "velocity": drone.velocity,
        "battery": drone.battery_status,
        "mission_status": drone.mission_status
    }

#현재 드론 상태 정보를 반환
def get_drone_status(): 
    return drone_statuses
