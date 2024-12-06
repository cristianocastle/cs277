from puppy_state import PuppyState
import state_asleep

class StatePlay(PuppyState):
    """
    Represents the state of a puppy when it is playing.
    """
    
    def feed(self, puppy):
        """
        Attempts to feed the puppy, but it is too busy playing.

        Args:
            puppy (Puppy): The puppy instance to feed.

        Returns:
            str: The reaction of the puppy to feeding.
        """
        return "The puppy is too busy playing with the ball to eat right now."

    def play(self, puppy):
        """
        Plays with the puppy and checks if it should fall asleep after playing too much.

        Args:
            puppy (Puppy): The puppy instance to play with.

        Returns:
            str: The reaction of the puppy to playing.
        """
        puppy.inc_plays()
        if puppy.plays >= 3:
            puppy.change_state(state_asleep.StateAsleep())
            return ("You throw the ball again and the puppy excitedly chases it.\n"
                    "The puppy played so much it fell asleep!")
        return "You throw the ball again and the puppy excitedly chases it."