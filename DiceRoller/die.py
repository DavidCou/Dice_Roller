import random

class Die:
    """A class representing a single die."""
    def __init__(self, num_sides=6):
        """Set the number of side the die has with a defualt side number of 6"""
        self.num_sides = num_sides

    def roll_die(self):
        """Roll the die and return a random value between 1 and the number of sides."""
        return random.randint(1, self.num_sides)