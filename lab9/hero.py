from entity import Entity
import random

class Hero(Entity):
    def basic_attack(self, opponent):
        dmg = random.randomint(1,6) + random.randint(1,6)
        opponent.take_damage(dmg)
        return f"{self._name} slashes {opponent._name} with thier sword for {dmg} damage!"

    def special_attack(self,opponent):
        dmg = random.randomint(1,12)
        opponent.take_damage(dmg)
        return f"{self._name} hit {opponent._name} with an arrow for {dmg} damage!"
