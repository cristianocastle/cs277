from abc import ABC, abstractmethod

class Plate(ABC):
    @abstractmethod
    def description(self) -> str:
        pass

    @abstractmethod
    def area(self) -> int:
        pass

    @abstractmethod
    def weight(self) -> int:
        pass
    
    @abstractmethod
    def count(self) -> int:
        pass
