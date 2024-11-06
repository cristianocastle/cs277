from door import Door
import random

class BasicDoor(Door):
    """
    A class representing a basic door that can be pushed or pulled to open.
    """

    def __init__(self):
        """
        Initializes the BasicDoor with a random solution.
        """
        self._solution = random.choice(["Push", "Pull"])
        self._input = 0

    def examine_door(self):
        """
        Provides a description of the door.

        Returns:
            str: A description of the door.
        """
        return "A basic door. You can either push or pull it to open."

    def menu_options(self):
        """
        Provides the menu options for interacting with the door.

        Returns:
            str: The menu options for interacting with the door.
        """
        return "1. Push\n2. Pull"

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
            option (int): The option chosen by the user (1 for Push, 2 for Pull).

        Returns:
            str: A message indicating the result of the attempt.
        """
        if option == 1:
            self._input = "Push"
        elif option == 2:
            self._input = "Pull"
        return f"You try to {self._input} the door."
    
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
        return "Try the other way."
    
    def success(self):
        """
        Provides a success message for opening the door.

        Returns:
            str: A success message for opening the door.
        """
        return f"The door opens."
