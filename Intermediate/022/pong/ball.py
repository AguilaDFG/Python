from turtle import Turtle
from random import randint
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.shapesize(0.5, 0.5)
        self.penup()
        self.setheading(randint(0,360))
        while 80<self.heading()<100 or 170<self.heading()<190 or 260<self.heading()<280 or not 10<self.heading()<350:
            self.setheading(randint(0, 360))
    def move(self):
        self.fd(10)
        if self.ycor()>380 or self.ycor()<-380:
            self.setheading(360-self.heading())
    def bounce(self):
        if self.heading()<180:
            self.setheading(180-self.heading())
        elif self.heading()>180:
            self.setheading(180-self.heading()+360)
