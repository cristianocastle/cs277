import abc
from abc import abstractmethod

class Entity(abc.ABC):
    """
    An abstract base class representing a generic entity in the game.

    Attributes:
        name (str): The name of the entity.
        _max_hp (int): The maximum health points of the entity.
        hp (int): The current health points of the entity.
    """
    
    def __init__(self, name, max_hp):
        """
        Initializes a new entity with a given name and maximum health points.

        Args:
            name (str): The name of the entity.
            max_hp (int): The maximum health points of the entity.
        """
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp  

    def take_damage(self, dmg):
        """
        Reduces the entity's health points by the specified damage amount.

        Args:
            dmg (int): The amount of damage to inflict.
        """
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0

    def heal(self):
        """
        Restores the entity's health points to the maximum health points.
        """
        self.hp = self.max_hp

    def __str__(self):
        """
        Returns a string representation of the entity, including its name and health points.

        Returns:
            str: A string representation of the entity.
        """
        return f"{self.name}\nHP:{self.hp}/{self.max_hp}"
    
    @abstractmethod
    def attack(self, entity) -> str:
        """
        Abstract method for attacking another entity. Must be implemented by subclasses.

        Args:
            entity (Entity): The entity to attack.
        """
        pass