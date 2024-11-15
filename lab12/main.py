# naithen ramirez, cris padilla
# 11/13/24
# This program is a Thanksgiving dinner plate simulator

from check_input import get_int_range
from small_plate import SmallPlate
from large_plate import LargePlate
from green_beans import GreenBeans
from pie import Pie
from potatoes import Potatoes
from stuffing import Stuffing
from turkey import Turkey


def examine_plate(plate): 
    """
    Examine the current state of the plate and provide feedback.

    This function displays the plate's contents, checks if the plate has failed
    (overflowed or collapsed), and provides hints about remaining space and weight capacity.

    Args:
        plate (Plate): The current plate object to examine.

    Returns:
        bool: True if the plate has failed (overflowed or collapsed), False otherwise.
    """
    # Display the plate's description
    print("\nCurrent plate contents:")
    print(plate.description())

    # Get remaining area and weight capacity
    area_remaining = plate.area()
    weight_remaining = plate.weight()

    # Check if the plate has failed
    if area_remaining <= 0:
        print("Your plate has overflowed! Food spills on the floor.")
        return True
    if weight_remaining <= 0:
        print("Your plate is too heavy! It collapses.")
        return True

    # Determine area hint
    if area_remaining >= 41:
        area_hint = "plenty"
    elif 21 <= area_remaining <= 40:
        area_hint = "some"
    else:  # 1-20
        area_hint = "a tiny bit"

    # Determine weight hint
    if weight_remaining >= 13:
        weight_hint = "strong"
    elif 7 <= weight_remaining <= 12:
        weight_hint = "weak"
    else:  # 1-6
        weight_hint = "bending"

    # Display the hints
    print(f"The plate is {weight_hint} and has {area_hint} of space left.")

    # Plate has not failed
    return False

def main():
    """
    Main function to run the Thanksgiving dinner plate simulator.

    This function manages the main game loop, allowing the user to choose a plate type,
    add food items, and monitors the plate's status until the user quits or the plate fails.
    """
    # Present the user with a menu to choose the base plate type
    print("- Thanksgiving Dinner -")
    print("Serve yourself as much food as you")
    print("like from the buffet, but make sure")
    print("that your plate will hold without")
    print("spilling everywhere!")
    print("Choose a plate:")
    print("1. Small Plate")
    print("2. Large Plate")
    base_plate_choice = get_int_range("Enter your choice: ", 1, 2)
    
    if base_plate_choice == 1:
        plate = SmallPlate()
    else:
        plate = LargePlate()
    
    item_count = 0
    spilled = False
    
    # Dictionary mapping choices to food classes
    food_options = {
        1: Turkey,
        2: Stuffing,
        3: Potatoes,
        4: GreenBeans,
        5: Pie
    }
    
    # Repeatedly prompt the user to add a new food item
    while True:
        print("\n1. Turkey")
        print("2. Stuffing")
        print("3. Potatoes")
        print("4. Green Beans")
        print("5. Pie")
        print("6. Quit")
        food_choice = get_int_range("Enter your choice: ", 1, 6)
        
        if food_choice == 6:
            # User decides to quit
            print("You decided to stop adding food.")
            break
        else:
            # Instantiate the food item and wrap it using the food class directly
            food_class = food_options[food_choice]
            plate = food_class(plate)
            item_count += 1
            # Call examine_plate to display the hint
            if examine_plate(plate):
                spilled = True
                print("You spilled your food on the floor!")
                break
    
    # If the user quits without spilling, display the final plate contents
    if not spilled:
        print("\nFinal plate contents:")
        print(plate.description())
        print(f"Good job! You made it to the table with {item_count} items.")
        print(f"Space remaining: {plate.area()} square inches")
        print(f"Weight remaining: {plate.weight()} ounces")

if __name__ == "__main__":
    main()