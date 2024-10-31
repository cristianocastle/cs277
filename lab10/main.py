#Naithen Ramirez, cris padilla 
# Oct 31, 2024 
# This program is a dungeon and monsters exploring game 

from hero import Hero
from enemy import Enemy
from map import Map
from check_input import get_int_range

def main():
    """
    Main function to run the dungeon and monsters exploring game.
    Prompts the user to enter their name, constructs the hero and map objects,
    and runs the game loop until the hero dies, finds the finish, or the user quits.
    """
    hero_name = input("What is your name traveler? ")
    hero = Hero(hero_name)
    game_map = Map()

    while True:
        # Display the current state of the map and hero
        print(game_map)
        print(hero)

        # Menu for the user to choose their next move
        print("1. Go North")
        print("2. Go South")
        print("3. Go East")
        print("4. Go West")
        print("5. Quit")
        choice = get_int_range("Enter your choice: ", 1, 5)

        # Move the hero based on the user's choice
        if choice == '1':
            hero.go_north()
        elif choice == '2':
            hero.go_south()
        elif choice == '3':
            hero.go_east()
        elif choice == '4':
            hero.go_west()
        elif choice == '5':
            break


if __name__ == "__main__":
    main()