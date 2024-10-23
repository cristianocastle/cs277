import abc

class Entity(abc.ABC):
    """
    An abstract base class representing a generic entity with health points (HP).
    
    Attributes:
        _name (str): The name of the entity.
        _max_hp (int): The maximum health points of the entity.
        _hp (int): The current health points of the entity.
    """
    
    def __init__(self, name, max_hp):
        """
        Initializes an Entity instance with a name and maximum health points.
        
        Args:
            name (str): The name of the entity.
            max_hp (int): The maximum health points of the entity.
        """
        self._name = name
        self._max_hp = max_hp
        self._hp = max_hp
    
    @property
    def name(self):
        """
        Gets the name of the entity.
        
        Returns:
            str: The name of the entity.
        """
        return self._name
    
    @property
    def hp(self):
        """
        Gets the current health points of the entity.
        
        Returns:
            int: The current health points of the entity.
        """
        return self._hp
    
    def take_damage(self, dmg):
        """
        Reduces the entity's health points by the specified damage amount.
        
        Args:
            dmg (int): The amount of damage to inflict on the entity.
        """
        self._hp -= dmg
        if self._hp < 0:
            self._hp = 0
    
    def __str__(self):
        """
        Returns a string representation of the entity's name and current health points.
        
        Returns:
            str: A string representing the entity's name and current health points.
        """
        return f"{self._name}: {self._hp}/{self._max_hp}"
    
    @abc.abstractmethod
    def basic_attack(self, opponent):
        """
        Performs a basic attack on the opponent.
        
        Args:
            opponent: The target of the basic attack.
        """
        pass

    @abc.abstractmethod
    def special_attack(self, opponent):
        """
        Performs a special attack on the opponent.
        
        Args:
            opponent: The target of the special attack.
        """
        pass