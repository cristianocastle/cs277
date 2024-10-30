class Map(): 
    _instance = None
    _initialized = False
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        if not Map._initialized:
            self.map = []
            with open("map1.txt", "r") as file:
                for line in file:
                    self.map.append(list(line.strip()))
            self._revealed = [[False for _ in row] for row in self.map]
            Map._initialized = True
    
    def __getitem__(self, row):
        return self.map[row]
    
    def __len__(self):
        return len(self.map)
    
    def show_map(self,loc):
        map_display = ""
        hero_row, hero_col = loc
        for i in range(5):  
            for j in range(5):  
                if (i, j) == (hero_row, hero_col):
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
        row, col = loc
        self._revealed[row][col] = True
    def remove_at_loc(self, loc):
        row, col = loc
        self.map[row][col] = "n"
        
