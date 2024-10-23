
# drone.py : 임의로 정의한 드론 상태 정보

drone_statuses = {}

#드론 클래스 정의
class Drone:
    def __init__(self, drone_id, position, battery_status):
        self.id = drone_id
        self.position = position
        self.battery_status = battery_status

    def __repr__(self):
        return f"Drone(id={self.id}, position={self.position}, battery={self.battery_status})"


#전역 드론 상태 딕셔너리에 드론 상태 업데이트
def update_drone_status(drone):
    drone_statuses[drone.id] = {
        "position": drone.position,
        "battery": drone.battery_status
    }

#현재 드론 상태 정보를 반환
def get_drone_status(): 
    return drone_statuses
