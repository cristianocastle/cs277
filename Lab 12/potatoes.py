from plate_decorator import PlateDecorator

class Potatoes(PlateDecorator):
    """
    A decorator class representing potatoes on a plate.

    This class extends the PlateDecorator to add potatoes to the plate,
    updating the plate's description, area, weight, and item count.
    """

    def description(self) -> str:
        """
        Get the updated description of the plate with potatoes added.

        Returns:
            str: The plate's description including "Potatoes".
        """
        base_description = super().description()
        if "with" in base_description:
            return base_description + " and Potatoes"
        else:
            return base_description + " with Potatoes"
    
    def area(self) -> int:
        """
        Calculate the remaining area on the plate after adding potatoes.

        Returns:
            int: The remaining area on the plate, reduced by 18 square units.
        """
        return super().area() - 18
    
    def weight(self) -> int:
        """
        Calculate the remaining weight capacity of the plate after adding potatoes.

        Returns:
            int: The remaining weight capacity, reduced by 6 units.
        """
        return super().weight() - 6
    
    def count(self) -> int:
        """
        Get the updated count of items on the plate after adding potatoes.

        Returns:
            int: The total number of items on the plate, increased by 1.
        """
