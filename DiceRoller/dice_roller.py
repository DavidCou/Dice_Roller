class DiceRoller:
    """A class that takes input from a user and creates and rolls dice based on the user input."""
    def __init__(self):
        self.dice = []
        self.dice_type_specs = {}
        self.dice_types_lists = {}

    def run(self):
        """Main method to run the dice roller."""
        print("Welcome to the Dice Roller!")
        while True:
            multi_dice_prompt = (
                "Would you like to create and roll multiple different sided dice at the same time? "
                "e.g. A D6 and a D10 (y/n): "
            )
            multiple_die_types = self.get_user_input_y_n(multi_dice_prompt)
            if multiple_die_types:
                self.get_dice_types()
                print(self.dice_type_specs)
            else:
                # Prompt the user for the dice specifucations
                num_sides_prompt = "How many dice would you like to roll? (Enter a whole number greater than 0): "
                num_dice_prompt = "How many sides should each die have? (Enter a whole number greater than 1): "    
                num_dice = self.get_user_num_input(num_sides_prompt, 1)
                num_sides = self.get_user_num_input(num_dice_prompt, 2)

                # Create and roll the dice
                self.create_single_dice_type(num_dice, num_sides)
                input(f"Press any key to roll your {num_dice} D{num_sides}: ")
                
                if num_dice > 1:
                    print(f"Rolling your D{num_sides}s...")
                    print(f"Your dice rolled a total of {self.roll_single_dice_type(num_dice)}")
                else:
                    print(f"Rolling your D{num_sides}...")
                    print(f"Your die rolled a {self.roll_single_dice_type(num_dice)}")
                
                self.ask_to_roll_again()
    
    def get_user_input_y_n(self, prompt):
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
    
    def get_dice_types(self):
        """Prompts the user for their dice types and adds them to a dictionary"""   
        num_types_prompt = "How many different types of die would you like to roll? (Enter a whole number greater than 1): "
        num_types = self.get_user_num_input(num_types_prompt, 2)
        num_sides_prompt = "How many sides should this die type have? (Enter a whole number greater than 1): "
        num_dice_prompt = "How many dice of this type would you like to roll? (Enter a whole number greater than 0): "
        
        # Collect the specifications for each die type and add them to the dictionary 
        for i in range(1, num_types):
            num_sides = self.get_user_num_input(num_sides_prompt, 2)
            num_dice = self.get_user_num_input(num_dice_prompt, 1)
            self.dice_type_specs[num_sides] = num_dice

    def get_user_num_input(self, prompt, min_value):
        """Prompt the user for input and validate it as an integer greater than or equal to min_value."""
        while True:
            try:
                value = int(input(prompt))
                if value < min_value:
                    raise ValueError(f"Value must be a whole number greater than or equal to {min_value}.")
                return value
            except ValueError as e:
                print(f"Invalid input! Please try again with a valid number.")

    def create_single_dice_type(self, num_dice, num_sides):
        """Create a list of Die objects based on user input."""
        from .die import Die  # Import Die class here instead of at the top of the file to avoid circular imports in __init__.py
        self.dice = [Die(num_sides) for _ in range(num_dice)]

    def roll_single_dice_type(self, num_dice):
        """Roll all dice of a single type."""
        if num_dice > 1:
            roll_total = 0
            for i, die in enumerate(self.dice, 1):
                current_roll = die.roll_die()
                roll_total += current_roll
                print(f"Die {i} rolled: {current_roll}")
            return roll_total
        else:
            return self.dice[0].roll_die()
    
    def ask_to_roll_again(self):
        """Ask the user if they want to roll again"""
        prompt = "Would you like to roll more dice? (y/n): "
        roll_again = self.get_user_input_y_n(prompt)
        if roll_again == False:
            print("Goodbye!")
            exit()