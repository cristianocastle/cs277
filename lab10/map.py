import os

class Map():
    """
    A singleton class representing the game map.

    Attributes:
        _instance (Map): The singleton instance of the Map class.
        _initialized (bool): A flag indicating whether the map has been initialized.
        map (list): A 2D list representing the game map.
        _revealed (list): A 2D list indicating which parts of the map have been revealed.
    """
    
    _instance = None
    _initialized = False

    def __new__(cls):
        """
        Ensures that only one instance of the Map class is created (singleton pattern).

        Returns:
            Map: The singleton instance of the Map class.
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        """
        Initializes the map by reading from a file and setting up the revealed status.
        This method is only executed once due to the singleton pattern.
        """
        if not Map._initialized:
            self.map = []
            file_path = os.path.join(os.path.dirname(__file__), "map1.txt")
            if not os.path.exists(file_path):
                print("Error: map1.txt not found.")
                self.map = []
                self._revealed = []
            else:
                with open(file_path, "r") as file:
                    for line in file:
                        self.map.append(list(line.strip()))
                self._revealed = [[False for _ in row] for row in self.map]
                Map._initialized = True
    
    def __getitem__(self, row):
        """
        Allows access to the map rows using indexing.

        Args:
            row (int): The index of the row to access.

        Returns:
            list: The specified row of the map.
        """
        return self.map[row]
    
    def __len__(self):
        """
        Returns the number of rows in the map.

        Returns:
            int: The number of rows in the map.
        """
        return len(self.map)
    
    def show_map(self, loc):
        """
        Displays a 5x5 portion of the map centered around the hero's location.

        Args:
            loc (tuple): The (row, column) location of the hero.

        Returns:
            str: A string representation of the 5x5 portion of the map.
        """
        map_display = ""
        hero_row, hero_col = loc


        for i in range(5):
            for j in range(5):
                if (i,j) == (hero_row,hero_col):
                    map_display += "* "
                elif 0 <= i < len(self.map) and 0 <= j < len(self.map[i]):
                    if self._revealed[i][j]:
                        map_display += self.map[i][j] + " "
                    else:
                        map_display += "x "
                else:
                    map_display += "x "
            map_display += "\n"
        return map_display.strip()
    
    def reveal (self,loc):
        """
        Sets the value in the 2D revealed list at the specified location to True.

        Parameters:
        loc (tuple): The (row, column) location to reveal.
        """
        row, col = loc
        self._revealed[row][col] = True
        
    def remove_at_loc(self, loc):
        """
        Overwrites the character in the map list at the specified location with an 'n'.

        Parameters:
        loc (tuple): The (row, column) location to remove.
        """
        row, col = loc
        self.map[row][col] = "n"
