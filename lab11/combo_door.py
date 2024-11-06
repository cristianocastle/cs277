from door import Door
import random

class ComboDoor(Door):
    """
    A class representing a combo door that has combination lock 1-10.
    """
    def __init__(self):
        """
        Initializes the ComboDoor with a random solution.
        """
        self._solution = random.randint(1,10)
        self._input = 0

    def examine_door(self):
        """
        Provides a description of the door.

        Returns:
            str: A description of the door.
        """
        return "A door with a combination lock. You can spin the dial to a number 1-10."

    def menu_options(self):
        """
        Provides the menu options for interacting with the door.

        Returns:
            str: The menu options for interacting with the door.
        """
        return "Enter # 1-10"

    def get_menu_max(self):
        """
        Returns the maximum number of menu options.

        Returns:
            int: The maximum number of menu options.
        """
        return 10

    def attempt(self, option):
        """
        Attempts to open the door with the given option.

        Parameters:
            option (int): The option chosen by the user 

        Returns:
            str: A message indicating the result of the attempt.
        """
        self._input = option
        return f"You turn the dial to... {self._input}"
    
    def is_unlocked(self):
        """
        Checks if the door is unlocked.

        Returns:
            bool: True if the door is unlocked, False otherwise.
        """
        return self._input == self._solution
    
    def clue(self):
        """
        Provides a clue for opening the door.

        Returns:
            str: A clue for opening the door.
        """
        if self._input < self._solution:
            return "Try a higher number."
        else:
            return "Try a lower number."
    
    def success(self):
        """
        Provides a success message for opening the door.

        Returns:
            str: A success message for opening the door.
        """
        return f"The door opens."
