# naithen ramirez, cris padilla
# 12/05/24
# this is a puppy simulator program that allows the user to feed or play with the puppy

from check_input import get_int_range
from puppy import Puppy

def main():
    puppy = Puppy()
    print("Congratualtion on your new puppy!")
    while True:
        #Menu
        print("\nWhat would you like to do?")
        print("1. Feed the puppy")
        print("2. Play with the puppy")
        print("3. Quit")

        choice = get_int_range("Enter choice: ", 1, 3)

        #Eating State
        if choice == 1:
            print(puppy.give_food())
        #Playing State
        elif choice == 2:
            print(puppy.throw_ball())
        #Quit
        elif choice == 3:
            break

if __name__ == "__main__":
    main()
