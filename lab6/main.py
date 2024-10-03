from player import Player
from check_input import get_yes_no

def take_turn(player):
    player.roll_dice()
    print(player)
    
    if player.has_three_of_a_kind():
        print("You got 3 of a kind!")
    elif player.has_pair():
        print("You got a pair!")
    elif player.has_series():
        print(f"You got a series of {player.dice[0].value}")
    else:
        print("Aww. Too Bad.")

    print(f"Score = {player.get_points()}")
    
def main():
    print("-Yahtzee-\n")
    player = Player()
    
    while True:
        take_turn(player)
        choice = get_yes_no("Play again?(Y/N):")
        print()
        if choice == False:
            print("Game Over.")
            print(f"Final Score:{player.get_points()}")
            break
        elif choice == True:
            continue


if __name__ == "__main__":
    main()