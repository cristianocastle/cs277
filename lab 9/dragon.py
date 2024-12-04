import abc
from entity import Entity
import random

class Dragon(Entity, abc.ABC):
    """
    An abstract base class representing a Dragon, inheriting from the Entity class.
    
    Attributes:
        _special_attacks (int): The number of special attacks the dragon can perform.
    
    Methods:
        decrement_special_attack(): Decrements the number of special attacks available.
        basic_attack(opponent): Performs a basic attack on the opponent.
        special_attack(opponent): Abstract method for performing a special attack on the opponent.
    """
    
    def __init__(self, name, max_hp, num_sp):
        """
        Initializes a Dragon instance with a name, maximum health points, and number of special attacks.
        
        Args:
            name (str): The name of the dragon.
            max_hp (int): The maximum health points of the dragon.
            num_sp (int): The number of special attacks the dragon can perform.
        """
        super().__init__(name, max_hp)
        self._special_attacks = num_sp
    
    def decrement_special_attack(self):
        """
        Decrements the number of special attacks available. Ensures the count does not go below zero.
        """
        self._special_attacks -= 1
        if self._special_attacks < 0:
            self._special_attacks = 0

    def basic_attack(self, opponent):
        """
        Performs a basic attack on the opponent by smashing with its tail.
        
        Args:
            opponent (Entity): The target of the basic attack.
        
        Returns:
            str: A string describing the attack and the damage dealt.
        """
        dmg = random.randint(3, 7)  # Corrected random.randomint to random.randint
        opponent.take_damage(dmg)
        return f"{self._name} smashes you with its tail for {dmg} damage!"
    
    def __str__(self):
        """
        Returns a string representation of the dragon's name, current health points, and special attacks left.
        
        Returns:
            str: A string representing the dragon's name, current health points, and special attacks left.
        """
        return f"{super().__str__()} (Special attacks left: {self._special_attacks})"

    @abc.abstractmethod
    def special_attack(self, opponent):
        """
        Abstract method for performing a special attack on the opponent.
        
        Args:
            opponent (Entity): The target of the special attack.
        """
        pass