import random

class Die:
    """
    Represents a single die with a specified number of sides.
    """
    def __init__(self, sides=6):
        """
        Initializes the Die with a specified number of sides and rolls it to set the initial value.
        
        Args:
            sides (int): The number of sides on the die. Default is 6.
        """
        self.sides = sides
        self.value = self.roll()

    def roll(self):
        """
        Rolls the die to generate a random value between 1 and the number of sides.
        
        Returns:
            int: The value rolled.
        """
        self.value = random.randint(1, self.sides)
        return self.value
    
    def __str__(self):
        """
        Returns the string representation of the die's value.
        
        Returns:
            str: The value of the die as a string.
        """
        return str(self.value)
    
    def __lt__(self, other):
        """
        Compares if the value of this die is less than the value of another die.
        
        Args:
            other (Die): Another die to compare against.
        
        Returns:
            bool: True if this die's value is less than the other die's value, False otherwise.
        """
        return self.value < other.value
    
    def __eq__(self, other):
        """
        Compares if the value of this die is equal to the value of another die.
        
        Args:
            other (Die): Another die to compare against.
        
        Returns:
            bool: True if this die's value is equal to the other die's value, False otherwise.
        """
        return self.value == other.value
    
    def __sub__(self, other):
        """
        Returns the difference between the value of this die and the value of another die.
        
        Args:
            other (Die): Another die to compare against.
        
        Returns:
            int: The difference between this die's value and the other die's value.
        """
        return self.value - other.value