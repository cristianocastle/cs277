from door_factory import DoorFactory
from basic_door import BasicDoor
from locked_door import LockedDoor
from combo_door import ComboDoor

class EasyDoorFactory(DoorFactory):
    
    def create_door(self):
        door_type = random.randint(1, 3)
        if door_type == 1:
            return BasicDoor()
        elif door_type == 2:
            return LockedDoor()
        else:
            return ComboDoor()