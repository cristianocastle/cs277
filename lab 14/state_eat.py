from puppy_state import PuppyState
import state_asleep
import state_play

class StateEat(PuppyState):
    """
    Represents the state of a puppy when it is eating.
    """

    def feed(self, puppy):
        """
        Feeds the puppy and checks if it should fall asleep after eating too much.

        Args:
            puppy (Puppy): The puppy instance to feed.

        Returns:
            str: The reaction of the puppy to feeding.
        """
        puppy.inc_feeds()
        if puppy.feeds >= 3:
            puppy.change_state(state_asleep.StateAsleep())
            return ("The puppy continues to eat as you add another scoop of kibble to its bowl.\n"
                    "The puppy ate so much it fell asleep.")
        return "The puppy continues to eat as you add another scoop of kibble to its bowl."

    def play(self, puppy):
        """
        Plays with the puppy and changes its state to playing.

        Args:
            puppy (Puppy): The puppy instance to play with.

        Returns:
            str: The reaction of the puppy to playing.
        """
        puppy.change_state(state_play.StatePlay())
        puppy.reset()
        puppy.inc_plays()
        return "The puppy looks up from its food and chases the ball you threw."