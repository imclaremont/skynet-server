import uuid

class Delivery:
  def __init__(self, content, origin, destination):
    self.delivery_id = str(uuid.uuid4())
    self.content = content
    self.origin = origin
    self.destination = destination
    self.is_reserved = False
    self.drone = None

  def __repr__(self) :
    return f"Delivery : {{content : {self.content}, origin : {self.origin}, destination : {self.destination}, is_reserved : {self.is_reserved}}}"