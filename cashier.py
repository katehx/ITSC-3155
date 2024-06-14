class Cashier:
    def __init__(self):
        pass


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
        return round(((dollars_large * 1.00) + (dollars_half * 0.50) + (quarters * 0.25) + (nickles * 0.05)), 2)


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