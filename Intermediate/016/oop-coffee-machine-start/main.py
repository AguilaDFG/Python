from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
on = True
while on:
    question = input(f"What would you want: {menu.get_items()}?").lower()
    if question == "report":
        coffee_maker.report()
        money_machine.report()
    if question == "off":
        on = False
    if question == "latte" or question == "espresso" or question == "cappuccino":
        drink = menu.find_drink(question)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)