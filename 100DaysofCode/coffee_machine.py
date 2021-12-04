# Day 15 Project
# Make 3 hot flavors
# Espresso {$1.50, 50 ml water, 18g coffee}, Latte{$2,50, 200 ml water, 24g coffee, 150 ml milk}, Capuccino {$3.00, 250ml water, 24g coffee, 100ml milk}
# Type report = resources

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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100

}


# "cappuccino": {

#     "ingredients": {

#         "water": 250,

#         "milk": 100,

#         "coffee": 24,

#     },

#     "cost": 3.0,

# }
profit = 0
# Print report
# CHeck resources sufficient

 # TODO - 3. Check resources sufficient
def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredient are insufficient"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]: # water[250] =  value 
            print(f"There is not enough {item}")
            return False
    return True
# TODO - 4. Process coins
def process_coins():

    """Returns the Total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01

    return total


# TODO - 5. CHeck the transaction successful

def is_transaction_successful(money_received, drink_cost):
    """Return true when the payment is accepted or False if money is insufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money Refunded")
        return False

def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️")


is_on = True

while is_on:

# TODO - 1. Prompt user by asking
    choice  = input("What would you like? (espresso, latte, cappuccino): ")
    if choice == "off":
        is_on = False
    # TODO - 2. Print Report
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
   
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])


        







