from plate import Plate

class SmallPlate(Plate):
    """
    A class representing a small plate, implementing the Plate interface.

    This class defines the properties and behaviors of a sturdy, 10-inch paper plate.
    """

    def description(self) -> str:
        """
        Get the description of the small plate.

        Returns:
            str: A string describing the small plate.
        """
        return "Sturdy 10-inch paper plate"
    
    def area(self) -> int:
        """
        Get the total available area of the small plate.

        Returns:
            int: The area of the plate in square units (78 square units).
        """
        return 78
    
    def weight(self) -> int:
        """
        Get the total weight capacity of the small plate.

        Returns:
            int: The weight capacity of the plate in weight units (32 units).
        """
        return 32
    
    def count(self) -> int:
        """
        Get the initial count of food items on the small plate.

        Returns:
            int: The number of food items on the plate (initially 0).
        """
        return 0