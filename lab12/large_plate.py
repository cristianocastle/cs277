from plate import Plate

class LargePlate(Plate):
    """
    A class representing a large plate, implementing the Plate interface.

    This class defines the properties and behaviors of a large, 12-inch paper plate.
    """

    def description(self) -> str:
        """
        Get the description of the large plate.

        Returns:
            str: A string describing the large plate.
        """
        return "Flimsy 12-inch paper plate"
    
    def area(self) -> int:
        """
        Get the total available area of the large plate.

        Returns:
            int: The area of the plate in square units (113 square units).
        """
        return 113
    
    def weight(self) -> int:
        """
        Get the total weight capacity of the large plate.

        Returns:
            int: The weight capacity of the plate in weight units (24 units).
        """
        return 24
    
    def count(self) -> int:
        """
        Get the initial count of food items on the large plate.

        Returns:
            int: The number of food items on the plate (initially 0).
        """
        return 0