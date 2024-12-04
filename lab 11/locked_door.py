from door import Door
import random

class LockedDoor(Door):
    """
    A class representing a locked door that requires finding a hidden key to open.
    """
    def __init__(self):
        """
        Initializes the LockedDoor with a random hiding spot for the key.
        """
        self._solution = random.choice(['mat', 'flower pot', 'fake rock'])
        self._input = 0

    def examine_door(self):
        """
        Provides a description of the door.

        Returns:
            str: A description of the door.
        """
        return "A locked door. Look around, the key is hidden nearby."

    def menu_options(self):
        """
        Provides the menu options for interacting with the door.

        Returns:
            str: The menu options for interacting with the door.
        """
        return "1. Look under the mat.\n2. Look under the flower pot.\n3. Look under the fake rock"

    def get_menu_max(self):
        """
        Returns the maximum number of menu options.

        Returns:
            int: The maximum number of menu options.
        """
        return 3

    def attempt(self, option):
        """
        Attempts to find the key in the specified hiding spot.

        Parameters:
            option (int): The option chosen by the user (1 for mat, 2 for flower pot, 3 for fake rock).

        Returns:
            str: A message indicating the result of the attempt.
        """
        if option == 1:
            self._input = 'mat'
        elif option == 2:
            self._input = 'flower pot'
        elif option == 3:
            self._input = 'fake rock'
        return f"You look under the {self._input}."

    def is_unlocked(self):
        """
        Checks if the door is unlocked.

        Returns:
            bool: True if the door is unlocked, False otherwise.
        """
        return self._input == self._solution

    def clue(self):
        """
        Provides a clue for finding the key.

        Returns:
            str: A clue for finding the key.
        """
        return "Try looking somewhere else."

    def success(self):
        """
        Indicates that the door has been successfully unlocked.

        Returns:
            str: A message indicating the door has been successfully unlocked.
        """
        return "You found the key and opened the door."