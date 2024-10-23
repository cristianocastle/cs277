import random
from check_input import get_int, get_positive_int, get_int_range
from fire_dragon import FireDragon
from flying_dragon import FlyingDragon
from flying_fire_dragon import FlyingFireDragon
from hero import Hero

def main():
    hero = Hero("Hero", 100)
    dragons = [FireDragon(), FlyingDragon(), FlyingFireDragon()]

    print("Welcome to dragon training, Hero!")
    print("You must defeat 3 Deagons.")
    while dragons and hero.hp > 0:
        print("\nChoose a dragon to attack:")
        for i, dragon in enumerate(dragons):
            print(f"{i + 1}. {dragon.name} {dragon.hp}")
        
        # Get the index of the dragon in the list
        dragon_choice = get_int_range("Enter the number of the dragon you want to attack: ", 1, len(dragons)) - 1
        # Get the dragon object from the list
        chosen_dragon = dragons[dragon_choice]

        print("\nChoose your attack:")
        print("1. Sword")
        print("2. Arrow")
        attack_choice = get_int_range("Enter the number of your attack choice: ", 1, 2)

        if attack_choice == 1:
            attack_message = hero.basic_attack(chosen_dragon)
        else:
            attack_message = hero.special_attack(chosen_dragon)
        
        print(attack_message)

        # if the dragon has been defeated, remove it from the list
        if chosen_dragon.hp == 0:
            print(f"{chosen_dragon.name} has been defeated!")
            dragons.pop(dragon_choice)

        # if the dragon is still alive, it will attack
        if dragons:
            attacking_dragon = random.choice(dragons)
            if random.choice([True, False]):
                attack_message = attacking_dragon.basic_attack(hero)
            else:
                attack_message = attacking_dragon.special_attack(hero)
            
            print(attack_message)

    if hero.hp > 0:
        print("Congratulations! You have defeated all the dragons.")
    else:
        print("You have been defeated by the dragons.")

if __name__ == "__main__":
    main()