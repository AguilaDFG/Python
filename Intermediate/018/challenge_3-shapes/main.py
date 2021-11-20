from turtle import Turtle, Screen
from random import randint
turtle = Turtle()
screen = Screen()
screen.colormode(255)
for a in range(3,11):
    turtle.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
    for b in range(a):
        turtle.fd(100)
        turtle.right(360/a)
screen.exitonclick()