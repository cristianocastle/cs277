# naithen ramirez, cris padilla
# 11/7/24
# this program is a escape room game

from check_input import get_int_range
from easy_door_factory import EasyDoorFactory
from difficult_door_factory import DifficultDoorFactory

def main():
    print("Welcome to the Escape Room.")
    print("You must unlock 3 doors to escape...")
    difficulty = get_int_range("(1. Easy 2. Hard): ", 1, 2)
    
    if difficulty == 1: # easy
        factory = EasyDoorFactory() # create a factory
        doors = [factory.create_door() for _ in range(3)] # create 3 doors
    elif difficulty == 2: # hard
        factory = DifficultDoorFactory() # create a factory
        doors = [factory.create_door() for _ in range(3)] # create 3 doors
        
        
        

    