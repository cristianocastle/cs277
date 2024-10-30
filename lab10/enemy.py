import random
from entity import Entity

class Enemy(Entity):
    """
    A class representing an enemy character in the game.

    Attributes:
        name (str): The name of the enemy.
        hp (int): The health points of the enemy.
    """
    
    def __init__(self):
        """
        Initializes a new enemy with a random name and random health points.

        Attributes:
            name (str): The name of the enemy, chosen randomly from a predefined list.
            hp (int): The health points of the enemy, chosen randomly between 4 and 8.
        """
        name = random.choice(["Goblin", "Vampire", "Ghoul", "Skeleton", "Zombie"])
        hp = random.randint(4, 8)
        super().__init__(name, hp)
    
    def attack(self, entity):
        """
        Attacks another entity, dealing random damage between 1 and 4.

        Args:
            entity (Entity): The entity to attack.

        Returns:
            str: A message describing the attack and the damage dealt.
        """
        damage = random.randint(1, 4)
        entity.take_damage(damage)
        return f"{self.name} attacks {entity.name} for {damage}"