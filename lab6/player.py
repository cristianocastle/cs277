from die import Die

class Player(Die):
    """
    Represents a player in the game, holding a list of dice and the player's points.
    """
    def __init__(self):
        """
        Initializes the Player with three Die objects and sets the initial points to 0.
        """
        self.dice = [Die(), Die(), Die()]
        self.dice.sort()
        self.points = 0
    
    def get_points(self):
        """
        Returns the player's current points.
        
        Returns:
            int: The player's points.
        """
        return self.points

    def roll_dice(self):
        """
        Rolls all dice for the player and sorts them.
        """
        for d in self.dice:
            d.roll()
        self.dice.sort()
   
    def has_pair(self):
        """
        Checks if the player has a pair of dice with the same value.
        Increments points by 1 if a pair is found.
        
        Returns:
            bool: True if a pair is found, False otherwise.
        """
        if self.dice[0] == self.dice[1] or self.dice[0] == self.dice[2] or self.dice[1] == self.dice[2]:
            self.points += 1
            return True
        else:
            return False

    def has_three_of_a_kind(self):
        """
        Checks if the player has three dice with the same value.
        Increments points by 3 if three of a kind is found.
        
        Returns:
            bool: True if three of a kind is found, False otherwise.
        """
        if self.dice[0] == self.dice[1] == self.dice[2]:
            self.points += 3
            return True
        else:
            return False

    def has_series(self):
        """
        Checks if the player has a series of dice values in sequence.
        Increments points by 2 if a series is found.
        
        Returns:
            bool: True if a series is found, False otherwise.
        """
        if (self.dice[1] - self.dice[0] == 1) and (self.dice[2] - self.dice[1] == 1):
            self.points += 2
            return True
        return False