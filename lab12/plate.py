from abc import ABC, abstractmethod

class Plate(ABC):
    """
    An abstract base class representing a plate.

    This class defines the interface for all types of plates in the system.
    Concrete implementations must provide implementations for all abstract methods.
    """

    @abstractmethod
    def description(self) -> str:
        """
        Get the description of the plate and its contents.

        Returns:
            str: A string describing the plate and the food items on it.
        """
        pass

    @abstractmethod
    def area(self) -> int:
        """
        Get the remaining area on the plate.

        Returns:
            int: The number of square units of area left on the plate.
        """
        pass

    @abstractmethod
    def weight(self) -> int:
        """
        Get the remaining weight capacity of the plate.

        Returns:
            int: The number of weight units the plate can still hold.
        """
        pass
    
    @abstractmethod
    def count(self) -> int:
        """
        Get the number of food items on the plate.

        Returns:
            int: The total count of food items currently on the plate.
        """
        pass