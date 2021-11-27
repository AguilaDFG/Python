from turtle import Turtle, Screen
from random import randint
screen = Screen()
on = False
screen.setup(500, 400)
colors = ["red", "orange", "yellow", "green", "blue", "purple", "black"]
y = -150
bet = screen.textinput("make your bet", "Which turtle is going to win? ")
turtles = []
for a in range(7):
    turtle = Turtle(shape="turtle")
    turtle.up()
    turtle.color(colors[a])
    turtle.goto(-230, y)
    turtles.append(turtle)
    y += 50
on = True
while on:
    for turtle in turtles:
        turtle.fd(randint(0,10))
        if turtle.xcor() >= 230:
            on = False
            if bet == turtle.pencolor():
                print("You win!")
            else:
                print("You lose")
            print(f"The winner was {turtle.pencolor()}")

screen.exitonclick()