
class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

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


 # Return the current amount for each of the resources
    def show_report(self):
        # Return bread inventory
        print(f'Bread: {self.machine_resources["bread"]} slice(s)')
        # Return ham inventory
        print(f'Ham: {self.machine_resources["ham"]} slice(s)')
        # Return cheese inventory
        print(f'Cheese: {self.machine_resources["cheese"]} slice(s)')
