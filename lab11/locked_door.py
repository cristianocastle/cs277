from door import Door
import random

class LockedDoor(Door):
    def __init__(self):
        self.solution = random.choice(['mat', 'flower pot', 'fake rock'])
        self.input = None

    def examine_door(self):
        return "You encountered a locked door, you should look aroung for the key."

    def menu_options(self):
        return "1. Look under the mat\n2. Look under the flower pot\n3. Look under the fake rock"

    def get_menu_max(self):
        return 3

    def attempt(self, option):
        if option == 1:
            self.input = 'mat'
        elif option == 2:
            self.input = 'flower pot'
        elif option == 3:
            self.input = 'fake rock'
        return f"You look under the {self.input}."

    def is_unlocked(self):
        return self.input == self.solution

    def clue(self):
        return "Look somewhere else."

    def success(self):
        return "You found the key and opened the door."
