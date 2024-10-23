import random
from dragon import Dragon
from fire import Fire

class FireDragon(Dragon, Fire):
    """
    A class representing a Fire Dragon, inheriting from the Dragon and Fire classes.
    
    Methods:
        __init__(): Initializes the Fire Dragon with a name, maximum health points, and number of special attacks.
        special_attack(opponent): Performs a special attack on the opponent using either fireball or fireblast.
    """
    
    def __init__(self):
        """
        Initializes a FireDragon instance with a name, maximum health points, and number of special attacks.
        """
        super().__init__(name="Fire Dragon", max_hp=20, num_sp=3)
    
    def special_attack(self, opponent):
        """
        Performs a special attack on the opponent using either fireball or fireblast.
        
        Args:
            opponent (Entity): The target of the special attack.
        
        Returns:
            str: A string describing the attack and the damage dealt.
        """
        attack = random.choice([self.fireball, self.fireblast])
        return attack(opponent)