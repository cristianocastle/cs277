from plate_decorator import PlateDecorator

class Stuffing(PlateDecorator):
    """
    A decorator class representing stuffing on a plate.

    This class extends the PlateDecorator to add stuffing to the plate,
    updating the plate's description, area, weight, and item count.
    """
    def description(self) -> str:
        """
        Get the updated description of the plate with stuffing added.

        Returns:
            str: The plate's description including "Stuffing".
        """
        base_description = super().description()
        if "with" in base_description:
            return base_description + " and Stuffing"
        else:
            return base_description + " with Stuffing"
    
    def area(self) -> int:
        """
        Calculate the remaining area on the plate after adding stuffing.

        Returns:
            int: The remaining area on the plate, reduced by 18 square units.
        """
        return super().area() - 18
    
    def weight(self) -> int:
        """
        Calculate the remaining weight capacity of the plate after adding stuffing.

        Returns:
            int: The remaining weight capacity, reduced by 7 units.
        """
        return super().weight() - 7
    
    def count (self) -> int:
        """
        Get the updated count of items on the plate after adding stuffing.

        Returns:
            int: The total number of items on the plate, increased by 1.
        """
        return super().count() + 1
        