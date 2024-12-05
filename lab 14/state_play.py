from puppy_state import PuppyState
import state_asleep


class StatePlay(PuppyState):
    def feed(self, puppy):
        return "The puppy is to busy to playing with the ball to eat right now."

    def play(self, puppy):
        puppy.inc_plays()
        if puppy.plays >= 3:
            puppy.change_state(state_asleep.StateAsleep())
            return (
                "You throw the ball again and the puppy excitedlly chases it.\n"
                "The puppy played so much it fell asleep!"
                )
        return "You throw the ball again and the puppy excitedlly chases it."
