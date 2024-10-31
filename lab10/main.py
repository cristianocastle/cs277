#Naithen Ramirez, cris padilla 
# Oct 31, 2024 
# This program is a dungeon and monsters exploring game 

from hero import Hero
from enemy import Enemy
from map import Map
from check_input import get_int_range
import random

def main():
    """
    Main function to run the dungeon and monsters exploring game.
    Prompts the user to enter their name, constructs the hero and map objects,
    and runs the game loop until the hero dies, finds the finish, or the user quits.
    """
    hero_name = input("What is your name, traveler? ")
    hero = Hero(hero_name)
    game_map = Map()

    while True:
        # Display the current state of the map and hero
        print(game_map.show_map((hero.location[0], hero.location[1])))
        print(hero)

        # Menu for the user to choose their next move
        print("1. Go North")
        print("2. Go South")
        print("3. Go East")
        print("4. Go West")
        print("5. Quit")
        choice = get_int_range("Enter your choice: ", 1, 5)

        # Move the hero based on the user's choice
        if choice == 1:
            result = hero.go_north()
        elif choice == 2:
            result = hero.go_south()
        elif choice == 3:
            result = hero.go_east()
        elif choice == 4:
            result = hero.go_west()
        elif choice == 5:
            print("You chose to quit the game. Goodbye!")
            break
        
        if result != 'o':   # type: ignore
            game_map.reveal((hero.location[0], hero.location[1]))

        # Encounter handling
        encounter = game_map[hero.location[0]][hero.location[1]]
        
        if encounter == 'm':  # Monster encounter
            enemy = Enemy()
            print(f"You encounter a {enemy.name}")
            print(enemy)

            while enemy.hp > 0:
                print(f"1. Attack {enemy.name}")
                print("2. Run Away")
                action = get_int_range("Enter choice: ", 1, 2)

                if action == 1:
                    attack = hero.attack(enemy)
                    print(attack)

                    if enemy.hp <= 0:
                        print(f"You have slain a {enemy.name}")
                        game_map.remove_at_loc((hero.location[0], hero.location[1]))
                        break  
                    
                    enemy_attack = enemy.attack(hero)
                    print(enemy_attack)

                    if hero.hp <= 0:
                        print(f"{hero.name} has died. Game over")
                        return
                elif action == 2:
                    print(f"{hero.name} ran away!")
                    directions = ["N", "S", "E", "W"]
                    random_dir = random.choice(directions)
                    if random_dir == "N":
                        hero.go_north()
                    elif random_dir == "S":
                        hero.go_south()
                    elif random_dir == "E":
                        hero.go_east()
                    elif random_dir == "W":
                        hero.go_west()
                    game_map.reveal((hero.location[0], hero.location[1]))
                    break
                else:
                    print("Invalid choice!")
        
        elif encounter == 'o':
            print("You cannot move in that direction.")
        elif encounter == 'n':
            print("This room is empty.")
        elif encounter == 's':
            print("You are back at the start of the dungeon.")
        elif encounter == 'i':
            if hero.hp == hero.max_hp:
                print("You found a health potion, but you already have full health.")
            else:
                print("You found a health potion and healed!")
                hero.heal()
            game_map.remove_at_loc((hero.location[0], hero.location[1]))
        elif encounter == 'f':
            print("Congratulations! You've found the exit and won the game!")
            break

if __name__ == "__main__":
    main()
