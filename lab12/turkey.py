from plate_decorator import PlateDecorator

class Turkey(PlateDecorator):
    """
    A decorator class representing turkey on a plate.

    This class extends the PlateDecorator to add turkey to the plate,
    updating the plate's description, area, weight, and item count.
    """
    def description(self):
        """
        Get the updated description of the plate with turkey added.

        Returns:
            str: The plate's description including "Turkey".
        """
        return super().description() + "Turkey"
    
    def area(self):
        """
        Calculate the remaining area on the plate after adding turkey.

        Returns:
            int: The remaining area on the plate, reduced by 18 square units.
        """
        return super().area() - 15
    
    def weight(self):
        """
        Calculate the remaining weight capacity of the plate after adding turkey.

        Returns:
            int: The remaining weight capacity, reduced by 4 units.
        """
        return super().weight() - 4
    
    def count (self):
        """
        Get the updated count of items on the plate after adding turkey.

        Returns:
            int: The total number of items on the plate, increased by 1.
        """
        return super().count() + 1