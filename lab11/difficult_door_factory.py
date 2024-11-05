from door_factory import DoorFactory
from combo_door import ComboDoor
from deadbolt_door import DeadboltDoor
from code_door import CodeDoor
import random

class DifficultDoorFactory(DoorFactory):
    
    def create_door(self):
        door_type = random.randint(1, 3)
        if door_type == 1:
            return ComboDoor()
        elif door_type == 2:
            return DeadboltDoor()
        else:
            return CodeDoor()