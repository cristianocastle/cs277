from entity import Entity
import random
from map import Map

class Hero(Entity):
    """
    A class representing a hero character in the game.

    Attributes:
        name (str): The name of the hero.
        health (int): The health points of the hero.
        location (list): The current location of the hero on the map.
    """
    
    def __init__(self, name):
        """
        Initializes a new hero with a given name and default health and location.

        Args:
            name (str): The name of the hero.
        """
        super().__init__(name, 25)
        self.location = [0, 0]
        
    def attack(self, entity):
        """
        Attacks another entity, dealing random damage between 2 and 5.

        Args:
            entity (Entity): The entity to attack.

        Returns:
            str: A message describing the attack and the damage dealt.
        """
        damage = random.randint(2, 5)
        entity.take_damage(damage)
        return f"{self.name} attacks {entity.name} for {damage}"
    

    def go_north(self):
        """
        Moves the hero one step to the north if within map bounds.

        Returns:
            list or str: The new location if the move was successful, 'o' if out of bounds.
        """
        if self.location[0] > 0:
            self.location = (self.location[0] - 1, self.location[1])
            return self.location
        else:
            return 'o'
    
    def go_south(self):
        """
        Moves the hero one step to the south if within map bounds.

        Returns:
            list or str: The new location if the move was successful, 'o' if out of bounds.
        """
        if self.location[0] < len(Map()) - 1:
            self.location = (self.location[0] + 1, self.location[1])
            return self.location
        else:
            return 'o'
    
    def go_east(self):
        """
        Moves the hero one step to the east if within map bounds.

        Returns:
            list or str: The new location if the move was successful, 'o' if out of bounds.
        """
        if self.location[1] < len(Map()[0]) - 1:
            self.location = (self.location[0], self.location[1] + 1)
            return self.location
        else:
            return 'o'
    
    def go_west(self):
        """
        Moves the hero one step to the west if within map bounds.
        Returns:
            list or str: The new location if the move was successful, 'o' if out of bounds.
        """
        if self.location[1] > 0:
            self.location = (self.location[0], self.location[1] - 1)
            return self.location
        else:
            return 'o'
        
        
        