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
        if self.special_attacks > 0:
            damage = random.randint(4, 8)
            opponent.take_damage(damage)
            self.special_attacks -= 1
            return f"The dragon swoops down and attacks the hero, dealing {damage} damage!"
        else:
            return "The dragon has no special attacks left and cannot use swoop."

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
        if self.special_attacks > 0:
            damage = random.randint(3, 7)
            opponent.take_damage(damage)
            self.special_attacks -= 1
            return f"The dragon blasts wind at the hero, dealing {damage} damage!"
        else:
            return "The dragon has no special attacks left and cannot use windblast."