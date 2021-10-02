import random
from art import logo
print(logo)
NUMBER = random.randint(1,100)
print("I'm thinking of a number between 1 and 100")
difficulty = input("Choose difficulty; 'easy'(10 attemps) or 'hard'(5 attemps): ").lower()
if difficulty == "easy":
    attemps = 10
else:
    attemps = 5
while attemps > 0:
    guess = int(input("Have a guess: "))
    if guess > NUMBER:
        print("Too high")
        attemps -= 1
        print(f"Attemps: {attemps}")
    elif guess < NUMBER:
        print("Too low")
        attemps -= 1
        print(f"Attemps: {attemps}")
    else:
        print(f"The number was {NUMBER}, you win")
        attemps = -1
    if attemps == 0:
        print(f"The number was {NUMBER}, you lose")