from plate_decorator import PlateDecorator

class Pie(PlateDecorator):
    """
    A decorator class representing a piece of pie on a plate.

    This class extends the PlateDecorator to add a piece of pie to the plate,
    updating the plate's description, area, weight, and item count.
    """
    def description(self) -> str:
        """
        Get the updated description of the plate with pie added.

        Returns:
            str: The plate's description including "Pie".
        """
        base_description = super().description()
        if "with" in base_description:
            return base_description + " and Pie"
        else:
            return base_description + " with Pie"
    
    def area(self) -> int:
        """
        Calculate the remaining area on the plate after adding a piece of pie.

        Returns:
            int: The remaining area on the plate, reduced by 19 square units.
        """
        return super().area() - 19
    
    def weight(self) -> int:
        """
        Calculate the remaining weight capacity of the plate after adding a piece of pie.

        Returns:
            int: The remaining weight capacity, reduced by 8 units.
        """
        return super().weight() - 8
    
    def count (self) -> int:
        """
        Get the updated count of items on the plate after adding a piece of pie.

        Returns:
            int: The total number of items on the plate, increased by 1.
        """
        return super().count() + 1