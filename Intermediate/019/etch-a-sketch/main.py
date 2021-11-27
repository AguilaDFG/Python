from turtle import Turtle, Screen
turtle = Turtle()
screen = Screen()
turtle.speed(0)
def forward():
    turtle.fd(10)
def back():
    turtle.back(10)
def right():
    turtle.rt(5)
def left():
    turtle.lt(5)
def clear():
    turtle.home()
    turtle.clear()
    turtle.st()
screen.listen()
screen.onkey(forward, "w")
screen.onkey(back, "s")
screen.onkey(left, "a")
screen.onkey(right, "d")
screen.onkey(clear, "c")
screen.exitonclick()