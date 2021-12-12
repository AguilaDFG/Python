from turtle import Turtle
class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=2.5, stretch_len=0.5)
        self.penup()
        self.goto(pos)
    def go_up(self):
        self.goto(self.xcor(), self.ycor()+20)
    def go_down(self):
        self.goto(self.xcor(), self.ycor()-20)