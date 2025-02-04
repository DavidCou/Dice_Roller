from random import randint

class Die:
    """A class representing a single die."""
    def __init__(self, num_sides):
        """Set the number of side the die has"""
        self.num_sides = num_sides

    def roll_die(self):
        return randint(1, self.num_sides)