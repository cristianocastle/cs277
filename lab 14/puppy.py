from state_asleep import StateAsleep

class Puppy:
    """
    Represents a puppy with various states and actions.
    """
    
    def __init__(self):
        """
        Initializes the Puppy object with default state, feeds, and plays.
        """
        self._state = StateAsleep()
        self._feeds = 0
        self._plays = 0

    @property
    def feeds(self):
        """
        Gets the number of feeds.
        """
        return self._feeds

    @property
    def plays(self):
        """
        Gets the number of plays.
        """
        return self._plays

    def change_state(self, new_state):
        """
        Updates the puppy's state to the new state.

        Args:
            new_state (str): The new state of the puppy.
        """
        self._state = new_state

    def throw_ball(self):
        """
        Calls the play method for the current state of the puppy.
        """
        return self._state.play(self)

    def give_food(self):
        """
        Calls the feed method for the current state of the puppy.
        """
        return self._state.feed(self)

    def inc_feeds(self):
        """
        Increments the number of times the puppy has been fed in a row.
        """
        self._feeds += 1

    def inc_plays(self):
        """
        Increments the number of times the puppy has played in a row.
        """
        self._plays += 1

    def reset(self):
        """
        Reinitialized the feeds and plays attributes.
        """
        self._feeds = 0
        self._plays = 0
