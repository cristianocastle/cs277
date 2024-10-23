import random

class Fire:
    '''
    A mixin class to represent fire-based attacks for a dragon.
    '''

    def fireblast(self, opponent):
        '''
        Blasts the opponent with fire if the dragon has any special attacks left.
        The opponent takes a random amount of damage in the range 5-9.
        The number of special attacks is decremented.

        Parameters:
        opponent (object): The opponent to attack.

        Returns:
        str: A description of the attack and the damage dealt, or a failure message.
        '''
        if self.special_attacks > 0:
            damage = random.randint(5, 9)
            opponent.take_damage(damage)
            self.special_attacks -= 1
            return f"The dragon blasts the hero with fire, dealing {damage} damage!"
        else:
            return "The dragon has no special attacks left and cannot use fireblast."

    def fireball(self, opponent):
        '''
        Spits a fireball at the opponent if the dragon has any special attacks left.
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
            return f"The dragon spits a fireball at the hero, dealing {damage} damage!"
        else:
            return "The dragon has no special attacks left and cannot use fireball."