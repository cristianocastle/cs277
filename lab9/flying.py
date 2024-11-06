import random

class Flying:
    '''
    A mixin class to represent flying-based attacks for a dragon.
    '''

    def swoop(self, opponent):
        '''
        Performs a swoop attack on the opponent if the dragon has any special attacks left.
        The opponent takes a random amount of damage in the range 4-8.
        The number of special attacks is decremented.

        Parameters:
        opponent (object): The opponent to attack.

        Returns:
        str: A description of the attack and the damage dealt, or a failure message.
        '''
        
        if self.special_attacks > 0: # type: ignore
            damage = random.randint(4, 8)
            opponent.take_damage(damage)
            self.special_attacks -= 1 # type: ignore # type: ignore
            return f"The {self._name} swoops down and attacks the hero, dealing {damage} damage!" # type: ignore # type: ignore
        else:
            return f"The {self._name} has no special attacks left and cannot use swoop." # type: ignore

    def windblast(self, opponent):
        '''
        Blasts wind at the opponent if the dragon has any special attacks left.
        The opponent takes a random amount of damage in the range 3-7.
        The number of special attacks is decremented.

        Parameters:
        opponent (object): The opponent to attack.

        Returns:
        str: A description of the attack and the damage dealt, or a failure message.
        '''
        if self.special_attacks > 0: # type: ignore # type: ignore
            damage = random.randint(3, 7)
            opponent.take_damage(damage)
            self.special_attacks -= 1 # type: ignore
            return f"The {self._name} blasts wind at the hero, dealing {damage} damage!" # type: ignore
        else:
            return f"The {self._name} has no special attacks left and cannot use windblast." # type: ignore
