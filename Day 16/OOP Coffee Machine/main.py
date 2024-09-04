from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import sys

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
#menu_item = MenuItem()

prompt_user = True
while prompt_user:

    options = menu.get_items()
    type_of_coffee = input(f"What would you like? {options}:")
    if type_of_coffee == "off":
        prompt_user = False
    elif type_of_coffee == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(type_of_coffee)

        resource_sufficient = coffee_maker.is_resource_sufficient(drink)

        if resource_sufficient:
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)

    



