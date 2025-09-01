from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True

coffee = CoffeeMaker()
menu = Menu()
money = MoneyMachine()

while is_on:
    user_input = input("What would you like? (espresso/latte/cappuccino/):")
    if user_input == "off":
        is_on = False
    elif user_input == "report":
        print(coffee.report())
        print(money.report())
    else:
        drink = menu.find_drink(user_input)
        if coffee.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                coffee.make_coffee(drink)