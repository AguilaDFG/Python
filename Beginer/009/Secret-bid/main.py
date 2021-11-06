def clear():
    print("\n"*100)
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)
bidders = {}
another = True
while another == True:
    name = input("What's your name? ")
    bid = float(input("What's your bid? $"))
    bidders[name] = bid
    other = input("Is there another participant?").lower()
    if other == "no":
        another = False
    clear()
    print(logo)
maxim = 0
winner = ""
for bidder in bidders:
    if bidders[bidder] > maxim:
        maxim = bidders[bidder]
        winner = bidder
    elif bidders[bidder] == maxim:
        winner += " and " + bidder
print(f"The winner is {winner} with a bid of {maxim}$")