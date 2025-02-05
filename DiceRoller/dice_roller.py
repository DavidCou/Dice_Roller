class DiceRoller:
    """A class that takes input from a user and creates and rolls dice based on the user input."""
    def __init__(self):
        self.dice = []

    def run(self):
        """Main method to run the dice roller."""
        print("Welcome to the Dice Roller!")
        while True:
            num_dice = self.get_user_input("How many dice would you like to roll? (Enter a whole number greater than 0): ", 1)
            num_sides = self.get_user_input("How many sides should each die have? (Enter a whole number greater than 1): ", 2)

            self.create_dice(num_dice, num_sides)
            input(f"Press enter to roll your {num_dice} D{num_sides}: ")
            self.roll_dice()

            roll_again = input("Would you like to roll more dice? (y/n): ").lower()
            if roll_again == "n":
                print("Thanks for playing!")
                break

    def get_user_input(self, prompt, min_value):
        """Prompt the user for input and validate it as an integer greater than or equal to min_value."""
        while True:
            try:
                value = int(input(prompt))
                if value < min_value:
                    raise ValueError(f"Value must be a whole number greater than or equal to {min_value}.")
                return value
            except ValueError as e:
                print(f"Invalid input! {e}")

    def create_dice(self, num_dice, num_sides):
        """Create a list of Die objects based on user input."""
        from .die import Die  # Import Die class here to avoid circular imports
        self.dice = [Die(num_sides) for _ in range(num_dice)]

    def roll_dice(self):
        """Roll all dice and display the results."""
        roll_total = 0
        for i, die in enumerate(self.dice, 1):
            current_roll = die.roll_die()
            roll_total += current_roll
            print(f"Die {i} rolled: {current_roll}")
        print(f"Total roll: {roll_total}")




                # # If only one die is to be rolled
                # die = Die(num_sides)
                # roll_die = input(f"Press enter to roll your {num_sides} sided die: ")
                # print(f"Your die rolled: {die.roll_die()}")