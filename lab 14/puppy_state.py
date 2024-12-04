from abc import ABC, abstractmethod

class PuppyState(ABC):
    @abstractmethod
    def feed(self, puppy):
        """
        Abstract method to feed the puppy.

        Args:
            puppy (Puppy): The puppy instance to feed.
        """
        pass

    @abstractmethod
    def play(self, puppy):
        """
        Abstract method to play with the puppy.

        Args:
            puppy (Puppy): The puppy instance to play with.
        """
        pass