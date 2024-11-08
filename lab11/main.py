# naithen ramirez, cris padilla
# 11/7/24
# this program is a escape room game

from check_input import get_int_range
from easy_door_factory import EasyDoorFactory
from difficult_door_factory import DifficultDoorFactory

def main():
    print("Welcome to the Escape Room.")
    print("You must unlock 3 doors to escape...") 
    difficulty = get_int_range("(1. Easy 2. Hard): ", 1, 2) # get difficulty level
    
    doors = [] # initialize list of doors
    if difficulty == 1: # easy
        factory = EasyDoorFactory() # create a factory
        doors = [factory.create_door() for _ in range(3)] # create 3 easy doors
    elif difficulty == 2: # hard
        factory = DifficultDoorFactory() # create a factory
        doors = [factory.create_door() for _ in range(3)] # create 3 hard doors
        
    for i in range(3): # for each door
        print(f"\nAttempting to open door {i+1}...")
        door = doors[i] # get the door
        print(door.examine_door()) # display door description

        while not door.is_unlocked(): # while the door is not unlocked
            print(door.menu_options()) # display menu
            choice = get_int_range("Enter your choice: ", 1, door.get_menu_max()) # get user choice
            print(door.attempt(choice)) # attempt to unlock the door

            if door.is_unlocked(): # if the door is unlocked
                print(door.success()) # display success message
            else: # if the door is not unlocked
                print(door.clue()) # display clue
                
    print("\nCongratulations! You escaped...this time.")
    
if __name__ == "__main__":
    main()
