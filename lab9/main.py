import random
from check_input import get_int, get_positive_int, get_int_range
from fire_dragon import FireDragon
from flying_dragon import FlyingDragon
from flying_fire_dragon import FlyingFireDragon
from hero import Hero

def main():
    print("What is your name challenger?")
    name = input()
    
    hero = Hero(name, 100)
    dragons = [FireDragon(), FlyingDragon(), FlyingFireDragon()]
    
        
    print(f"Welcome to dragon training, {hero.name}!")
    print("You must defeat 3 dragons.")
    
    # Continue the game while dragon and hero are alive
    while dragons and hero.hp > 0:
        
        
        print(f"\n{hero.name}: {hero.hp}")
        #TODO print hp / maxhp 
        
        for i, dragon in enumerate(dragons):
            print(f"{i + 1}. {dragon.name}: {dragon.hp}")
            #TODO print the dragon's special attacks left
    
        print("\nChoose a dragon to attack:")
        
        # Get the index of the dragon in the list
        dragon_choice = get_int_range("Enter the number of the dragon you want to attack: ", 1, len(dragons)) - 1
        # Get the dragon object from the list
        chosen_dragon = dragons[dragon_choice]

        print("\nAttack with:")
        print("1. Sword (2 D6)")
        print("2. Arrow (1 D12)")
        attack_choice = get_int_range("Enter the number of your attack choice: ", 1, 2)

        if attack_choice == 1:
            attack_message = hero.basic_attack(chosen_dragon)
        elif attack_choice == 2:
            attack_message = hero.special_attack(chosen_dragon)
        
        print(attack_message)

        #TODO add dragon attack

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