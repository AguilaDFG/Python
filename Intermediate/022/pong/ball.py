from turtle import Turtle
from random import randint
class Ball(Turtle):
    def __init__(self):
        super().__init__()
<<<<<<< HEAD
        self.color("white")
        self.shape("circle")
        self.shapesize(0.5, 0.5)
        self.penup()
        self.setheading(randint(0,360))
        while 80<self.heading()<100 or 170<self.heading()<190 or 260<self.heading()<280 or not 10<self.heading()<350:
            self.setheading(randint(0, 360))
    def move(self):
        self.fd(15)
        if not -390<self.ycor()<390:
=======
        self.shape("circle")
        self.shapesize(0.5, 0.5)
        self.pu()
        self.color("white")
        self.setheading(randint(0,360))
        while 80<self.heading()<100 or 170<self.heading()<190 or 260<self.heading()<280 or not 10<self.heading()<370:
            self.setheading(randint(0, 360))
    def move(self):
        self.fd(10)
        if self.ycor()>380 or self.ycor()<-380:
>>>>>>> day 22
            self.setheading(360-self.heading())
    def bounce(self):
        if self.heading()<180:
            self.setheading(180-self.heading())
<<<<<<< HEAD
        elif self.heading()>180:
            self.setheading(180-self.heading()+360)
=======
        if self.heading()>180:
            self.setheading(180-self.heading()+360)
        self.fd(10)
>>>>>>> day 22
