COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
import random
import scoreboard
from turtle import Turtle
class CarManager:
    def __init__(self):
        self.cars = []
        for n in range(10):
            self.create_car(random.randint(0,280), random.randint(-240, 280))
    def create_car(self, startx, starty):
        car = Car(random.choice(COLORS), STARTING_MOVE_DISTANCE + (MOVE_INCREMENT*scoreboard.level), (startx, starty))
        self.cars.append(car)
class Car(Turtle):
    def __init__(self, color, move, start):
        super().__init__()
        self.shape("square")
        self.shapesize(1, 2)
        self.pu()
        self.setheading(180)
        self.goto(start)
        self.color(color)
        self.move_dis = move
    def move(self):
        self.fd(self.move_dis)