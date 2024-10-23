import random
from dragon import Dragon
from flying import Flying
class FireDragon(Dragon,Flying):
    def __init__(self):
        super().__init__(name = "Flying Dragon", max_hp = 15, num_sp = 3)
    def speical_attack(self,opponent):
        attack = random.choice([self.swoop, self.windblast])
        return attack(opponent)