from turtle import  Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.pu()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed(0)
        self.go_to_ran()
    def go_to_ran(self):
        self.goto(random.randint(-280, 280), random.randint(-280, 280))
