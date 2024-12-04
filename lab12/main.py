# naithen ramirez, cris padilla
# 11/13/24
# This program is a Thanksgiving dinner plate simulator that allows the user to choose a base plate and add items to it until it fails.
from check_input import get_int_range
from small_plate import SmallPlate
from large_plate import LargePlate
from green_beans import GreenBeans
from pie import Pie
from potatoes import Potatoes
from stuffing import Stuffing
from turkey import Turkey


def examine_plate(plate): 
    """Displays the plate's description and hints about its remaining capacity."""
    description = plate.description()

    # Display the description
    print(description)
    # Get remaining area and weight capacity
    area_remaining = plate.area()
    weight_remaining = plate.weight()

    # Check if the plate has failed
    if area_remaining <= 0:
        print("Your plate isnt big enough for this much food! Your food spills over the edge.")
        return True
    if weight_remaining <= 0:
        print("Your plate is too heavy! It collapses.")
        return True

    # Determine area hint
    if area_remaining >= 41:
        area_hint = "Plenty"
    elif 21 <= area_remaining <= 40:
        area_hint = "Some"
    else:  # 1-20
        area_hint = "A tiny bit"

    # Determine weight hint
    if weight_remaining >= 13:
        weight_hint = "Strong"
    elif 7 <= weight_remaining <= 12:
        weight_hint = "Weak"
    else:  # 1-6
        weight_hint = "Bending"

    # Display the hints
    print(f"Sturdiness: {weight_hint}")
    print(f"Space available: {area_hint}")

    # Plate has not failed
    return False


def main():
    """Main function for the Thanksgiving Dinner game."""
    # Present the user with a menu to choose the base plate type
    print("- Thanksgiving Dinner -")
    print("Serve yourself as much food as you")
    print("like from the buffet, but make sure")
    print("that your plate will hold without")
    print("spilling everywhere!")
    print("Choose a plate:")
    print("1. Small Sturdy Plate")
    print("2. Large Flimsy Plate")
    base_plate_choice = get_int_range("Enter your choice: ", 1, 2)
    
    # Create the selected plate
    if base_plate_choice == 1:
        plate = SmallPlate()
    else:
        plate = LargePlate()
    
    # Initialize variables
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
            
            # Call examine_plate to display the hint and check if plate fails
            if examine_plate(plate):
                spilled = True
                print("You spilled your food on the floor!")
                break
    
    # If the user quits without spilling, display the final plate contents
    if not spilled:
        print("\nFinal plate contents:")
        print(plate.description())
        print(f"Good job! You made it to the table with {item_count} items.")
        print(f"There was still {plate.area()} square inches left on your plate.")
        print(f"Your plate could have held {plate.weight()} more ounces of food")
        print("Dont worry, you always go back for more. Happy Thanksgiving!")


if __name__ == "__main__":
    main()
