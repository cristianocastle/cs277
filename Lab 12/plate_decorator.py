from abc import ABC
from plate import Plate

class PlateDecorator(Plate, ABC):
    """
    An abstract base class for plate decorators.

    This class implements the Plate interface and serves as a base for all
    plate decorators. It wraps a Plate object and delegates all method calls to it.
    """

    def __init__(self, plate: Plate):
        """
        Initialize the PlateDecorator with a Plate object.

        Args:
            plate (Plate): The Plate object to be decorated.
        """
        self._plate = plate

    def description(self) -> str:
        """
        Get the description of the wrapped plate.

        Returns:
            str: The description of the wrapped plate.
        """
        return self._plate.description()
    
    def area(self) -> int:
        """
        Get the remaining area of the wrapped plate.

        Returns:
            int: The remaining area on the wrapped plate.
        """
        return self._plate.area()
    
    def weight(self) -> int:
        """
        Get the remaining weight capacity of the wrapped plate.

        Returns:
            int: The remaining weight capacity of the wrapped plate.
        """
        return self._plate.weight()
    
    def count(self) -> int:
        """
        Get the number of items on the wrapped plate.

        Returns:
            int: The number of items on the wrapped plate.
        """
        return self._plate.count()