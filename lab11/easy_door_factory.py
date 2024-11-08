from door_factory import DoorFactory
from basic_door import BasicDoor
from locked_door import LockedDoor
from combo_door import ComboDoor
import random

class EasyDoorFactory(DoorFactory):
    
    def create_door(self):
        doors = [BasicDoor, LockedDoor, ComboDoor]
        return random.choice(doors)()