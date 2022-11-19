# Coffee Machine

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    'americano': {
        'ingredients': {
            'water': 65,
            'coffee': 18,
        },
        'cost': 1.5,
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
    },
    'mocha': {
        'ingredients': {
            'water': 250,
            'milk': 50,
            'chocolate': 50,
            'coffee': 24,
        },
        'cost': 3.5,
    }
}

profit = 0  # machine has no money in it
resources = {
    "water": 300,
    "milk": 200,
    "chocolate": 100,
    "coffee": 100,
}

def is_resource_sufficient(order_ingredients):
    '''Returns True when order can be made, False if ingredients insufficient'''
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    '''Returns the total calculated from coins inserted.'''
    print('Please insert coins.')
    total = int(input('how many quarters?: ')) * 0.25
    total += int(input('how many dimes?: ')) * 0.1
    total += int(input('how many nickles?: ')) * 0.05
    total += int(input('how many pennies?: ')) * 0.01
    return total


def is_transaction_successful(money_reveived, drink_cost):
    '''Return True when the payment is accepted, or False if money is in sufficient.'''
    if money_reveived >= drink_cost:
        change = round(money_reveived - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit  #profit is a global variable
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
    return False


def make_coffee(drink_name, order_ingredients):
    '''Deduct the required ingredients from the resources. '''
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕")



is_on = True

while is_on:
    ask = input('What would you like to drink? (espresso/latte/cappuccino/mocha): ')
    if ask == 'off':
        is_on = False
    elif ask == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Chocolate: {resources['chocolate']}ml")
        print(f"Coffee: {resources['coffee']}ml")
        print(f"Money: ${profit}")
    else:
        drink = MENU[ask]
        if is_resource_sufficient(drink['ingredients']):
            payment = process_coins()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(ask, drink['ingredients'])










