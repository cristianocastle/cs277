from puppy_state import PuppyState
import state_eat

class StateAsleep(PuppyState):
    """
    Represents the state of a puppy when it is asleep.
    """

    def feed(self, puppy):
        """
        Feeds the puppy and changes its state to eating.

        Args:
            puppy (Puppy): The puppy instance to feed.

        Returns:
            str: The reaction of the puppy to feeding.
        """
        puppy.change_state(state_eat.StateEat())
        puppy.reset()
        puppy.inc_feeds()
        return "The puppy wakes up and comes running to eat."

    def play(self, puppy):
        """
        Attempts to play with the puppy, but it is asleep.

        Args:
            puppy (Puppy): The puppy instance to play with.

        Returns:
            str: The reaction of the puppy to playing.
        """
        return "The puppy is asleep. It doesn't want to play right now."