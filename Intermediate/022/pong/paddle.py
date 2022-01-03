from turtle import Turtle
class Paddle(Turtle):
<<<<<<< HEAD
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
=======
    def __init__(self, player):
        super().__init__()
        self.pu()
        self.shape("square")
        self.shapesize(0.5, 2)
        if player == 1:
            self.goto(-390, 0)
        else:
            self.goto(390, 0)
        self.setheading(90)
        self.color("white")
    def move(self):
        self.fd(10)
        if self.ycor() > 360:
            self.down()
        if self.ycor() < -360:
            self.up()
    def up(self):
        self.setheading(90)
    def down(self):
        self.setheading(270)
>>>>>>> day 22
