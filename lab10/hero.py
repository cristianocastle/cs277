from entity import Entity
import random
from map import Map


class Hero(Entity):
    
    def __init__(self, name):
        super().__init__(name, 100)
        location = [0, 0]
        
    def attack(self, entity):
        entity.take_damage(random.randint(2, 5))
        return f"{self.name} attacks {entity.name}!"
    
    def direction(self):
        
        #TODO requires map to be implemented
        