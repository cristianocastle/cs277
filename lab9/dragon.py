import abc
from entity import Entity
import random
class Dragon(Entity,abc.ABC):
    def __init__(self, name, max_hp, num_sp):
        super().__init__(name,max_hp)
        self._special_attacks = num_sp
    
    def decrement_special_attack(self):
        self._special_attacks -= 1
        if self._special_attacks < 0:
            self._special_attacks = 0

    def basic_attack(self, opponent):
        dmg = random.randomint(3,7)
        opponent.take_damage(dmg)
        return f"{self._name} smashes you with its tail for {dmg} damage!"
    def __str__(self):
        return f"{super().__str__()} (Special attacks left: {self._special_attacks})"
