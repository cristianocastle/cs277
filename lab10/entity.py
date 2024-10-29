import ABC 

class Entity(ABC):
    
    def __init__(self, name, max_hp):   
        self.name = name
        self._max_hp = max_hp

    def take_damage(self, dmg):
        pass

    def heal(self)
        pass

    def __str__(self):
        return f"{self.name}: {self.hp}/{self._max_hp}"
    
    def attack(self, entity):
        pass