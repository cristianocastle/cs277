from door_factory import DoorFactory
from combo_door import ComboDoor
from deadbolt_door import DeadboltDoor
from code_door import CodeDoor
import random

class DifficultDoorFactory(DoorFactory):
    
    def create_door(self):
        doors = [ComboDoor, DeadboltDoor, CodeDoor]
        return random.choice(doors)()