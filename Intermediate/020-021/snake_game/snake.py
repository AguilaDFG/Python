from turtle import Turtle
DISTANCE = 20
class Snake:
    def __init__(self):
        self.snake_body = []
        body0 = Turtle(shape="square")
        body0.color("white")
        body0.pu()
        self.snake_body.append(body0)
        self.head = self.snake_body[0]
        self.expand()
        self.expand()
    def move(self):
        for b in range(len(self.snake_body)-1, 0, -1):
            self.snake_body[b].goto(self.snake_body[b - 1].xcor(), self.snake_body[b - 1].ycor())
        self.head.fd(DISTANCE)
    def expand(self):
        body = Turtle(shape="square")
        body.color("white")
        body.pu()
        if self.head.heading() == 0:
            body.goto(self.head.xcor() + 20, self.head.ycor())
        if self.head.heading() == 90:
            body.goto(self.head.xcor(), self.head.ycor() + 20)
        if self.head.heading() == 180:
            body.goto(self.head.xcor() - 20, self.head.ycor())
        if self.head.heading() == 270:
            body.goto(self.head.xcor(), self.head.ycor() - 20)
        self.snake_body.insert(0, body)
        self.head = self.snake_body[0]
    def up(self):
        if not self.head.heading() == 270:
            self.head.setheading(90)
    def down(self):
        if not self.head.heading() == 90:
            self.head.setheading(270)
    def right(self):
        if not self.head.heading() == 180:
            self.head.setheading(0)
    def left(self):
        if not self.head.heading() == 0:
            self.head.setheading(180)
