from turtle import Turtle, Screen
from random import randint
turtle = Turtle()
screen = Screen()
screen.setworldcoordinates(0,0,490,490)
screen.colormode(255)
turtle.up()
turtle.speed(0)
turtle.hideturtle()
for a in range(10):
    turtle.goto(0,a*50)
    for b in range(10):
        turtle.dot(20, (randint(0,255), randint(0,255), randint(0,255)))
        turtle.fd(50)
screen.exitonclick()