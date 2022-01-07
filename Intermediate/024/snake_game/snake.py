from turtle import Turtle
DISTANCE = 20
START_POS = [(0,0), (-20,0), (-40,0)]
class Snake:
    def __init__(self):
        self.snake_body = []
        self.create()
    def create(self):
        for a in range(3):
            body0 = Turtle(shape="square")
            body0.color("white")
            body0.pu()
            body0.goto(START_POS[a])
            self.snake_body.append(body0)
        self.head = self.snake_body[0]
    def move(self):
        for b in range(len(self.snake_body)-1, 0, -1):
            self.snake_body[b].goto(self.snake_body[b - 1].xcor(), self.snake_body[b - 1].ycor())
        self.head.fd(DISTANCE)
    def expand(self):
        body = Turtle(shape="square")
        body.color("white")
        body.pu()
        body.goto(self.snake_body[-1].position())
        self.snake_body.append(body)
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
    def reset(self):
        for body in self.snake_body:
            body.goto(400, 0)
        self.snake_body.clear()
        self.create()

