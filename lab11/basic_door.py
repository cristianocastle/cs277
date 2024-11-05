from door import Door
import random

class BasicDoor(Door):
    def __init__(self):
        self.solution = random.choice({"Push", "Pull"})
        self.input = None
    def examine_door(self):
        return "A basic door. You can either push or pull it to open."
    
    def menu_options(self):
        return "1. Push\n2. Pull"
    
    def get_menu_max(self):
        return 2
    def attempt(self, option):
        if option == 1:
            self.input == "Push"
        elif option == 2:
            self.input== "Pull"
        return f"You try to {self.input} the door."
    
    def is_unlocked(self):
        return self.input == self.solution
    
    def clue(self):
        return "Try the other way."
    
    def success(self):
        return super().successful()
