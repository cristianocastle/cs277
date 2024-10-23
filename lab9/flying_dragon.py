import random
from dragon import Dragon
from flying import Flying

class FireDragon(Dragon, Flying):
    """
    A class representing a Fire Dragon that can fly and perform special attacks.
    
    Inherits from:
        Dragon: Base class for all dragons.
        Flying: Mixin class providing flying capabilities.
    """
    
    def __init__(self):
        """
        Initializes a FireDragon instance with a specific name, maximum HP, and number of special points.
        """
        super().__init__(name="Flying Dragon", max_hp=15, num_sp=3)
    
    def special_attack(self, opponent):
        """
        Performs a special attack on the opponent by randomly choosing one of the available flying attacks.
        
        Args:
            opponent: The target of the special attack.
        
        Returns:
            The result of the chosen attack on the opponent.
        """
        attack = random.choice([self.swoop, self.windblast])
        return attack(opponent)