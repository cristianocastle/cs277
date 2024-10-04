from player import Player
from check_input import get_yes_no

def take_turn(player):
    """
    Takes a turn for the player by rolling dice, displaying results, and updating score.
    
    Args:
        player (Player): The player object taking the turn.
    """
    player.roll_dice() # Roll the dice
    print(player) # Display the dice
    
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
    """
    Main function to start the Yahtzee game, manage turns, and handle game continuation.
    """
    print("-Yahtzee-\n")
    player = Player() # Create a new player
    
    while True:
        take_turn(player) # Take a turn for the player
        choice = get_yes_no("Play again?(Y/N):") # Ask user if they want to play again
        print()
        if choice == False:
            print("Game Over.")
            print(f"Final Score:{player.get_points()}")
            break
        elif choice == True:
            continue

if __name__ == "__main__":
    main()