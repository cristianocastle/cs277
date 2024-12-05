from puppy_state import PuppyState
import state_asleep
import state_play

class StateEat(PuppyState):
    def feed(self, puppy):
        puppy.inc_feeds()
        if puppy.feeds >= 3:
            puppy.change_state(state_asleep.StateAsleep())
            return (
                "The puppy continues to eat as you add another scoop of kibble to its bowl.\n"
                "The puppy ate so much it fell asleep.")
        return "The puppy continues to eat as you add another scoop of kibble to its bowl."

    def play(self, puppy):
        puppy.change_state(state_play.StatePlay())
        puppy.reset()
        puppy.inc_plays()
        return "The puppy looks up from its food and chases the ball you threw."
