STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
from turtle import Turtle
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.pu()
        self.setheading(90)
        self.goto(STARTING_POSITION)
    def move(self):
        self.fd(MOVE_DISTANCE)
    def level_up(self):
        self.goto(STARTING_POSITION)