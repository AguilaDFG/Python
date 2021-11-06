from data import MENU
from data import resources
def coffee(type):
    if MENU[type]["ingredients"]["water"] > resources["water"]:
        print("Sorry, there is not enough water")
    if MENU[type]["ingredients"]["milk"] > resources["milk"]:
        print("Sorry, there is not enough milk")
    if MENU[type]["ingredients"]["coffee"] > resources["coffee"]:
        print("Sorry, there is not enough coffee")
    if MENU[type]["ingredients"]["water"] <= resources["water"] and MENU[type]["ingredients"]["milk"] <= resources["milk"] and MENU[type]["ingredients"]["coffee"] <= resources["coffee"]:
        penny = int(input("Insert pennies"))
        dime = int(input("Insert dimes"))
        nickle = int(input("Insert nickles"))
        quarter = int(input("insert quarter"))
        payment = 0.01 * penny + 0.1 * dime + 0.05 * nickle + 0.25 * quarter
        if MENU[type]["cost"] > payment:
            print("Sorry, that's not enough money. Money refunded")
        elif MENU[type]["cost"] <= payment:
            exchange = round((payment - MENU[type]["cost"]), 2)
            print(f"Here is ${exchange} in exchange")
            resources["money"] += round((payment - exchange), 2)
            resources["water"] -= MENU[type]["ingredients"]["water"]
            resources["milk"] -= MENU[type]["ingredients"]["milk"]
            resources["coffee"] -= MENU[type]["ingredients"]["coffee"]
            print(f"Here is you {type}")
on = True
while on:
    question = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if question == "off":
        on = False
    elif question == "report":
        print(f'water: {resources["water"]} mL')
        print(f'milk: {resources["milk"]} mL')
        print(f'coffee: {resources["coffee"]} g')
        print(f'money: $ {resources["money"]}')
    elif question == "espresso":
        coffee("espresso")
    elif question == "latte":
        coffee("latte")
    elif question == "cappuccino":
        coffee("cappuccino")


