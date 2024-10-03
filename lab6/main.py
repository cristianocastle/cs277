from player import Player
from check_input import get_yes_no

def take_turn(player):
    
        print("-Yahtzee-")
        player.roll_dice()
        print(player)
        if player.has_three_of_a_kind():
            print("Three of a kind!")
        elif player.has_pair():
            print("Pair!")
        elif player.has_series():
            print("Series!")
        print("Points: ", player.get_points())
        return player.get_points()


def main():
    
    while True: 
        
        # p1 is an instance of the Player class
        p1 = Player()
        take_turn(p1)
        
        
        choice = get_yes_no("Play again? (yes/no): ")
        if choice == False:
            break
        elif choice == True:
            continue
        






if __name__ == "__main__":
    main()
    
    
    