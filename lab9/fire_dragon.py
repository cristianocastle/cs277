import random
from dragon import Dragon
from fire import Fire
class FireDragon(Dragon,Fire):
    def __init__(self):
        super().__init__(name = "Fire Dragon", max_hp =20, num_sp = 3)
    def speical_attack(self,opponent):
        attack = random.choice([self.fireball, self.fireblast])
        return attack(opponent)