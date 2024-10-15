
import random

class Vehicle(): 
    
    def __init__(self, name, initial, min_speed, max_speed):
        self.name = name
        self.initial = initial
        self.min_speed = min_speed
        self.max_speed = max_speed
        self.position = 0 
        self.energy = 100
    
    def fast(self, dist): 
        if self.energy >= 5:
            spaces_moved = random.randint(self.min_speed, self.max_speed)
            self.energy -= 5
            if spaces_moved > dist:
                self.position += spaces_moved
            else:
                self.position = dist - 1 
        return self.name, self.position 
                
            
    def slow(self, dist): 
        pass
    
    def __str__(self):
        pass
    
    def description_string(self):
        pass
    
    def special_move(self, dist):
        pass
    