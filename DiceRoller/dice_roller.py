class DiceRoller:
    """A class that takes input from a user and creates and rolls dice based on the user input."""
    def __init__(self):
        self.dice = []

    def run(self):
        """Main method to run the dice roller."""
        print("Welcome to the Dice Roller!")
        while True:
            multi_dice_prompt = (
                "Would you like to create and roll multiple different sided dice? "
                "e.g. A D6 and a D10 (Enter 'y' for yes and 'n' for no)"
            )
            multiple_die_types = self.is_one_dice_type(multi_dice_prompt)
            # if multiple_die_types:
            #     num_dice_types = 
            num_dice = self.get_user__num_input("How many dice would you like to roll? (Enter a whole number greater than 0): ", 1)
            num_sides = self.get_user__num_input("How many sides should each die have? (Enter a whole number greater than 1): ", 2)

            self.create_dice(num_dice, num_sides)
            input(f"Press any key to roll your {num_dice} D{num_sides}: ")
            self.roll_dice(num_dice)
            self.ask_to_roll_again()
    
    def is_one_dice_type(self, prompt):
        """Prompt the user for input, validate the responce and send a boolean value back if valid"""
        while True:
            try:
                responce = input(prompt)
                if responce == "y":
                    return True
                elif responce == 'n':
                    return False
                else:
                    raise ValueError("Invalid input! Enter either 'y' or 'n'.")
            except ValueError as e:
                print(e)
            
    def get_user__num_input(self, prompt, min_value):
        """Prompt the user for input and validate it as an integer greater than or equal to min_value."""
        while True:
            try:
                value = int(input(prompt))
                if value < min_value:
                    raise ValueError(f"Value must be a whole number greater than or equal to {min_value}.")
                return value
            except ValueError as e:
                print(f"Invalid input! Please try again with a valid number.")
    
    # def get_user_type_input(self, num_dice)

    def create_dice(self, num_dice, num_sides):
        """Create a list of Die objects based on user input."""
        from .die import Die  # Import Die class here instead of at the top of the file to avoid circular imports in __init__.py
        self.dice = [Die(num_sides) for _ in range(num_dice)]

    def roll_dice(self, num_dice):
        """Roll all dice and display the results."""
        if num_dice > 1:
            roll_total = 0
            for i, die in enumerate(self.dice, 1):
                current_roll = die.roll_die()
                roll_total += current_roll
                print(f"Die {i} rolled: {current_roll}")
            print(f"Your dice rolled for a total of {roll_total}")
        else:
            roll = self.dice[0].roll_die()
            print(f"Your die rolled a {roll}")
    
    def ask_to_roll_again(self):
        """Ask the user if they want to roll again"""
        while True:
            roll_again = input("Would you like to roll more dice? (y/n): ").lower()
            if roll_again == "y":
                break 
            elif roll_again == "n":
                print("Goodbye!")
                exit()
            else:
                print("Invalid input! Please enter 'y' to roll again or 'n' to exit.")