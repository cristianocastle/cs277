from die import Die

class Player(Die):
    def __init__(self):
        self.dice = [Die(),Die(),Die()]
        self.dice.sort()
        self.points = 0
    
    def get_points(self):
        return self.points

    def roll_dice(self):
        for d in self.dice:
            d.roll()
        self.dice.sort()
   
    def has_pair(self):
        if self.dice[0] == self.dice[1] or self.dice[0] == self.dice[2] or self.dice[1] == self.dice[2]:
            self.points += 1
            return True
        else:
            return False
    def has_three_of_a_kind(self):
        if self.dice[0] == self.dice[1] == self.dice[2]:
            self.points += 3
            return True
        else:
            return False
    def has_series(self):
        if (self.dice[1] - self.dice[0] == 1) and (self.dice[2] - self.dice[1] == 1):
            self.points += 2
            return True
        return False
    def __str__(self):
        return f"D1={self.dice[0]}, D2={self.dice[1]}, D3={self.dice[2]}"