from turtle import  Turtle, Screen
turtle = Turtle()
screen = Screen()
for a in range(15):
    turtle.down()
    turtle.fd(10)
    turtle.up()
    turtle.fd(10)
screen.exitonclick()