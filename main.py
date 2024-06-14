import data
from sandwich_maker import SandwichMaker
from cashier import Cashier

# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()

def main():
    order = ""
    while order != "off":
        # Initial prompt for user - formatted to lowercase to standardize the response
        order = (input("What would you like?(small/medium/large/off/report): ")).lower()

        if order == 'off':
            break
        elif order == 'report':
            sandwich_maker_instance.show_report()
        else:
            if sandwich_maker_instance.check_resources(recipes[order]["ingredients"]):
                coins = cashier_instance.process_coins()
                if cashier_instance.transaction_result(coins, recipes[order]["cost"]):
                    sandwich_maker_instance.make_sandwich(order, recipes[order]["ingredients"])
    print("Machine will now turn off.")

if __name__ == "__main__":
    main()
