from puppy_state import PuppyState
import state_eat


class StateAsleep(PuppyState):
    def feed(self, puppy):
        puppy.change_state(state_eat.StateEat())
        puppy.reset()
        puppy.inc_feeds()
        return "The puppy wakes up and comes running to eat."

    def play(self, puppy):
        return "The puppy is asleep. It doesn't want to play right now."
    
