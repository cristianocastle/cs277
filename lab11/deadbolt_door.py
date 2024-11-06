from typing import Literal
from door import Door
import random

class DeadboltDoor(Door):
    """
    A class representing a deadbolt door that has two deadbolts.
    """
    def __init__(self):
        """
        Initializes the DeadboltDoor with a random solution.
        """
        self._bolt1 = random.choice(['locked', 'unlocked'])
        self._bolt2 = random.choice(['locked', 'unlocked'])
        
    def examine_door(self):
        """
        Provides a description of the door.

        Returns:
            str: A description of the door.
        """
        return "A double deadbolt door. Both need to be unlocked to open the door."

    def menu_options(self):
        """
        Provides the menu options for interacting with the door.

        Returns:
            str: The menu options for interacting with the door.
        """
        return "1. Toggle deadbolt 1\n2. Toggle deadbolt 2"

    def get_menu_max(self):
        """
        Returns the maximum number of menu options.

        Returns:
            int: The maximum number of menu options.
        """
        return 2

    def attempt(self, option):
        """
        Attempts to open the door with the given option.

        Parameters:
            option (int): The option chosen by the user 

        Returns:
            str: A message indicating the result of the attempt.
        """
        self._input = option
        return f"You toggle bolt {self._input}"
    
    def is_unlocked(self):
        """
        Checks if the door is unlocked.

        Returns:
            bool: True if the door is unlocked, False otherwise.
        """
        return self._bolt1 == self._bolt2
    
    def clue(self): # type: ignore
        """
        Provides a clue for opening the door.

        Returns:
            str: A clue for opening the door.
        """
        if self._bolt1 == 'unlocked' or self._bolt2 == 'unlocked':
            return "You jiggle the door... it seems like one of the bolts is unlocked."
        elif self._bolt1 == 'locked' and self._bolt2 == 'locked':
            return "...it seems like it's completely locked."

    def success(self):
        """
        Provides a success message for opening the door.

        Returns:
            str: A success message for opening the door.
        """
        return f"The door opens."
