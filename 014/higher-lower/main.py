import random
import art
from game_data import data
b = random.randint(0,len(data)-1)
next = True
score = 0
def correct_answer():
    if data[a]['follower_count'] > data[b]['follower_count']:
        return "a"
    elif data[a]['follower_count'] < data[b]['follower_count']:
        return "b"
def compare():
    if correct_answer() == answer:
        global score
        score += 1
        return "Correct"
    else:
        global next
        next = False
        return "Incorrect"
clear = "\n" * 100
print(art.logo)
while next:
    a = b
    b = random.randint(0,len(data)-1)
    while data[a]['follower_count'] == data[b]['follower_count']:
        b = random.randint(0,len(data)-1)
    print(f"Compare A: {data[a]['name']}, {data[a]['description']}, {data[a]['country']}")
    print(art.vs)
    print(f"Against B: {data[b]['name']}, {data[b]['description']}, {data[b]['country']}")
    answer = input("Who has more followers? Type 'A' or 'B': ").lower()
    print(clear)
    print(art.logo)
    print(f"{compare()}! Score: {score}")