from entity import Entity
import random

class Hero(Entity):
    """
    A class representing a Hero, inheriting from the Entity class.
    
    Methods:
        basic_attack(opponent): Performs a basic attack on the opponent.
        special_attack(opponent): Performs a special attack on the opponent.
    """
    
    def basic_attack(self, opponent):
        """
        Performs a basic attack on the opponent by slashing with a sword.
        
        Args:
            opponent (Entity): The target of the basic attack.
        
        Returns:
            str: A string describing the attack and the damage dealt.
        """
        dmg = random.randint(1, 6) + random.randint(1, 6)
        opponent.take_damage(dmg)
        return f"{self._name} slashes {opponent._name} with their sword for {dmg} damage!"

    def special_attack(self, opponent):
        """
        Performs a special attack on the opponent by hitting with an arrow.
        
        Args:
            opponent (Entity): The target of the special attack.
        
        Returns:
            str: A string describing the attack and the damage dealt.
        """
        dmg = random.randint(1, 12)
        opponent.take_damage(dmg)
        return f"{self._name} hit {opponent._name} with an arrow for {dmg} damage!"