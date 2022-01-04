from turtle import Turtle
class Paddle(Turtle):
    def __init__(self, player):
        super().__init__()
        self.pu()
        self.shape("square")
        self.shapesize(0.5, 2)
        self.goto(player)
        self.setheading(90)
        self.color("white")
    def up(self):
        self.setheading(90)
        self.fd(10)
    def down(self):
        self.setheading(270)
        self.fd(10)