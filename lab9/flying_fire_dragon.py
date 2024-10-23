import random
from dragon import Dragon
from flying import Flying
from fire import Fire

class FlyingFireDragon(Dragon, Flying, Fire):
    """
    A class representing a Fire Dragon that can fly and use fire attacks.
    
    Inherits from:
        Dragon: Base class for all dragons.
        Flying: Mixin class providing flying capabilities.
        Fire: Mixin class providing fire-based attacks.
    """
    
    def __init__(self):
        """
        Initializes a FireDragon instance with a specific name, maximum HP, and number of special points.
        """
        super().__init__(name="Flying Fire Dragon", max_hp=10, num_sp=3)
    
    def special_attack(self, opponent):
        """
        Performs a special attack on the opponent by randomly choosing one of the available attacks.
        
        Args:
            opponent: The target of the special attack.
        
        Returns:
            The result of the chosen attack on the opponent.
        """
        attack = random.choice([self.swoop, self.windblast, self.fireblast, self.fireball])
        return attack(opponent)