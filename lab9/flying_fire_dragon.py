import random
from dragon import Dragon
from flying import Flying
from fire import Fire
class FireDragon(Dragon,Flying,Fire):
    def __init__(self):
        super().__init__(name = "Flying Fire Dragon", max_hp = 10, num_sp = 3)
    def speical_attack(self,opponent):
        attack = random.choice([self.swoop, self.windblast, self.fireblast, self.fireball])
        return attack(opponent)