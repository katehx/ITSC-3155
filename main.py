### Data ###

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 8,  ## slice
            "ham": 10,  ## slice
            "cheese": 14,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

class SandwichMachine:

    ### Set up machine with avaiable resources
    def __init__(self, machine_resources):
        self.machine_resources = machine_resources


    # Main method for running the machine, will loop until machine is turned off
    def run_machine(self):
        order = ""
        while order != "off":
            # Initial prompt for user - formatted to lowercase to standardize the response
            order = (input("What would you like?(small/medium/large/off/report): ")).lower()

            if order == 'off':
                break
            elif order == 'report':
                self.show_report()
            else:
                if self.check_resources(recipes[order]["ingredients"]):
                    coins = self.process_coins()
                    if self.transaction_result(coins, recipes[order]["cost"]):
                        self.make_sandwich(order, recipes[order]["ingredients"])
        print("Machine will now turn off.")


    # Return the current amount for each resource
    def show_report(self):
        # Return bread inventory
        print(f'Bread: {self.machine_resources["bread"]} slice(s)')
        # Return ham inventory
        print(f'Ham: {self.machine_resources["ham"]} slice(s)')
        # Return cheese inventory
        print(f'Cheese: {self.machine_resources["cheese"]} slice(s)')

    # Step through each of the ingredients and compare the recipie to current resources
    def check_resources(self, ingredients):

        # Check if there is enough bread
        if ingredients["bread"] <= self.machine_resources["bread"]:
            # Check if there is enough ham
            if ingredients["ham"] <= self.machine_resources["ham"]:
                # Check if there is enough cheese
                if ingredients["cheese"] <= self.machine_resources["cheese"]:
                    # All three ingredients check passed
                    return True
                else:
                    # Fail - not enough cheese
                    print("Sorry there is not enough cheese.")
                    return False
            else:
                # Fail - not enough ham
                print("Sorry there is not enough ham.")
                return False
        else:
            # Fail - not enough bread
            print("Sorry there is not enough bread.")
            return False


    # Calculate the total from coins inserted
    def process_coins(self):

        # Prompt user to provide payment - collect everything as a float for later multiplication
        print("Please insert coins.")
        # Large dollars
        dollars_large = float(input("How many large dollars?: "))
        # Half dollars
        dollars_half = float(input("How many half dollars?: "))
        # Quarters
        quarters = float(input("How many quarters?: "))
        # Nickles
        nickles = float(input("How many nickles?: "))

        # Total up the worth and return - use round function to keep 2 decimal places always (money!)
        return round(((dollars_large * 1.00) + (dollars_half * 0.50) + (quarters * 0.25) + (nickles * 0.05)),2)


    # Determine whether funds are sufficient and calculate change if needed
    def transaction_result(self, coins, cost):
        # Check if enough (or more than enough) money has been inserted
        if coins >= cost:
            # Calculate and return change, return true for sufficient funds
            print(f"Here is ${coins - cost} in change.")
            return True
        else:
            # Refund fully and return false for insufficient funds
            print(f"Sorry that's not enough money. ${coins} refunded.")
            return False


    # Step through each ingredient and deduct ingredients from recipie
    def make_sandwich(self, sandwich_size, order_ingredients):
        # Remove bread from resources
        self.machine_resources["bread"] -= order_ingredients["bread"]
        # Remove ham from resources
        self.machine_resources["ham"] -= order_ingredients["ham"]
        # Remove cheese from resources
        self.machine_resources["cheese"] -= order_ingredients["cheese"]
        # Print for completed sandwich
        print(f'{sandwich_size.capitalize()} sandwich is ready. Bon appetit!')






### Make an instance of SandwichMachine class and write the rest of the codes ###

# Create sandwich machine instance
machine = SandwichMachine(resources)

# Run machine
machine.run_machine()



