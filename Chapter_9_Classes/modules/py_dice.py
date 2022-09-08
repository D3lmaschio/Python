"""
This module shoud be used to represent a Dice."
There are no really random number here, only pseudonumber.
"""

from random import randint


class Dice:
    """This class must be used to represent a Dice."""

    def __init__(self, sides=3):
        """What does:
        Initialize the attributes from instance of class Dice.
        - The dice must have at least 3 sides.
        """
        if sides >= 3:
            self.sides = sides
        else:
            self.sides = 3

    def roll_dice(self, times=1):
        """Simulates rolling a dice. Returns the result of roll."""
        if times > 0:
            result = randint(1, self.sides)
        else:
            result = []
            for time in range(0, times)
            result.append(randint(1, self.sides))

        return result
