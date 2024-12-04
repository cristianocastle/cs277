from abc import ABC, abstractmethod

class DoorFactory(ABC):
    
    @abstractmethod
    def create_door(self) -> object:
        pass
