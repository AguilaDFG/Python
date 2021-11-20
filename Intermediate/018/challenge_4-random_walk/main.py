from turtle import Turtle, Screen
from random import randint
turtle = Turtle()
screen = Screen()
screen.colormode(255)
for a in range(50,randint(100,200)):
    turtle.setheading(90*randint(0,4))
    turtle.speed(a/20)
    turtle.pensize(a/20)
    turtle.pencolor(randint(0,255), randint(0,255), randint(0,255))
    turtle.fd(10)
screen.exitonclick()