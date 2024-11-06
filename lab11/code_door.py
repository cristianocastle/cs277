from door import Door
import random

class CodeDoor(Door):
    """
    A class representing a code door that has a code lock with three characters.
    """
    def __init__(self):
        """
        Initializes the CodeDoor with a random 3-character solution consisting of 'X' or 'O'.
        """
        self._solution = ''.join(random.choice(['X', 'O']) for _ in range(3))
        self._input = ''

    def examine_door(self):
        """
        Provides a description of the door.

        Returns:
            str: A description of the door.
        """
        return "A door with a coded keypad with three characters. Each key toggles a value with an 'X' or 'O'."

    def menu_options(self):
        """
        Provides the menu options for interacting with the door.

        Returns:
            str: The menu options for interacting with the door.
        """
        return "1. Press key 1\n2. Press key 2\n3. Press key 3"

    def get_menu_max(self):
        """
        Returns the maximum number of menu options.

        Returns:
            int: The maximum number of menu options.
        """
        return 3

    def attempt(self, option):
        """
        Attempts to open the door with the given code.

        Parameters:
            option (str): The code entered by the user.

        Returns:
            str: A message indicating the result of the attempt.
        """
        self._input = option
        solution_list = list(self._solution)
        if self._input == '1':
            if solution_list[0] == 'X':
                solution_list[0] = 'O'
            else:
                solution_list[0] = 'X'
        elif self._input == '2':
            if solution_list[1] == 'X':
                solution_list[1] = 'O'
            else:
                solution_list[1] = 'X'
        elif self._input == '3':
            if solution_list[2] == 'X':
                solution_list[2] = 'O'
            else:
                solution_list[2] = 'X'
        self._solution = ''.join(solution_list)
        return f"You toggle key {self._input}."

    def is_unlocked(self):
        """
        Checks if the door is unlocked.

        Returns:
            bool: True if the door is unlocked, False otherwise.
        """
        return self._input == self._solution

    def clue(self): # type: ignore
        """
        Provides a clue for opening the door.

        Returns:
            str: A clue for opening the door.
        """
        clue = list(self._solution)
        return clue
    
    def success(self):
        """
        Provides a success message for opening the door.

        Returns:
            str: A success message for opening the door.
        """
        return f"The door opens."