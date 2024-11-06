from abc import ABC, abstractmethod

class Door(ABC):
    
    @abstractmethod
    def examine_door(self) -> str:
        pass

    @abstractmethod
    def menu_options(self) -> str:
        pass

    @abstractmethod
    def get_menu_max(self) -> int:
        pass

    @abstractmethod
    def attempt(self, option) -> str:
        pass

    @abstractmethod
    def is_unlocked(self) -> bool:
        pass

    @abstractmethod
    def clue(self) -> str:
        pass

    @abstractmethod
    def success(self) -> str:
        pass
    
