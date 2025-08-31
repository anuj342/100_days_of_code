# MENU: Coffee types with ingredients and cost
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

# Resources: Starting stock of ingredients
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resources_enough(other_ingredients):
    for item in other_ingredients:
        if other_ingredients[item] > resources[item]:
            print(f"Not enough {item}.")
            return False
    return True

def process_coins():
    quarter = int(input("Enter number of quarters: "))
    dimes = int(input("Enter number of dimes: "))
    nickels = int(input("Enter number of nickels: "))
    pennies = int(input("Enter number of pennies: "))
    total = quarter *0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01 
    return total

def deduct_resources(ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]

profit = 0
is_on = True

while True:
    
    choice = input("What would you likes (espresso/latte/cappuccino): ")
    if choice == 'off':
        is_on = False
        break
    elif choice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        ingredients = drink["ingredients"]
        other_ingredients = is_resources_enough(drink["ingredients"])
        payment = process_coins()
        if payment < drink["cost"]:
            print("Not enough money. Money refunded.")
        else:
            change = payment - drink["cost"]
            print(f"Here is your change: {change:.2f}")
            profit += drink["cost"]
            deduct_resources(ingredients)
            print("Here is your latte ☕. Enjoy!")
            

