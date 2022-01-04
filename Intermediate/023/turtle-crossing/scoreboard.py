FONT = ("Courier", 12, "normal")
level = 0
from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.ht()
        self.goto(-250, 250)
        self.color("black")
        self.write(arg=f"level: {level}", align="center", font=FONT)
    def level_up(self):
        global level
        level += 1
        self.clear()
        self.write(arg=f"level: {level}", align="center", font=FONT)
    def gameover(self):
        self.goto(0,0)
        self.write(arg="GAME OVER", align="center", font=FONT)