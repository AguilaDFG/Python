from turtle import Turtle, Screen
from random import  randint
turtle = Turtle()
screen = Screen()
turtle.speed(0)
screen.colormode(255)
r = randint(10,360)
for a in range(1,r):
    turtle.pencolor(randint(0,255), randint(0,255), randint(0,255))
    turtle.circle(100)
    turtle.right(360/r)
screen.exitonclick()