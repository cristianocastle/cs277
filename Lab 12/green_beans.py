from plate_decorator import PlateDecorator

class GreenBeans(PlateDecorator):
    """
    A decorator class representing green beans on a plate.

    This class extends the PlateDecorator to add green beans to the plate,
    updating the plate's description, area, weight, and item count.
    """
    def description(self) -> str:
        """
        Get the updated description of the plate with green beans added.

        Returns:
            str: The plate's description including "Green beans".
        """
        base_description = super().description()
        if "with" in base_description:
            return base_description + " and Green beans"
        else:
            return base_description + " with Green beans"
    
    def area(self) -> int:
        """
        Calculate the remaining area on the plate after adding green beans.

        Returns:
            int: The remaining area on the plate, reduced by 20 square units.
        """
        return super().area() - 20
    
    def weight(self) -> int:
        """
        Calculate the remaining weight capacity of the plate after adding green beans.

        Returns:
            int: The remaining weight capacity, reduced by 3 units.
        """
        return super().weight() - 3
    
    def count (self) -> int:
        """
        Get the updated count of items on the plate after adding green beans.

        Returns:
            int: The total number of items on the plate, increased by 1.
        """
        return super().count() + 1