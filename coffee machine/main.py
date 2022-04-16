MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0
resources = {
    "water": 3000,
    "milk": 2000,
    "coffee": 500,
}


def is_sufficient(drink_resource):
    """Return true if resources is sufficient or false if resources insufficient"""
    for item in drink_resource:
        if resources[item] <= drink_resource[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Returns true if payment > coffee drink cost."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        global profit
        profit += drink_cost
        print(f"Here is ${change}dollars in change.")
        return True
    else:
        return False


def make_coffee(coffee_choice, ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your ☕️ {coffee_choice}. Enjoy!")


is_on = True
r

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino):").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water : {resources['water']}")
        print(f"Milk : {resources['milk']}")
        print(f"Coffee : {resources['coffee']}")
        print(f"Profit : {profit}")
    else:
        drink = MENU[choice]
        if is_sufficient(drink['ingredients']):
            payment = process_coins()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(choice, drink['ingredients'])