from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.ht()
        self.pu()
        self.speed(0)
        self.color("white")
        self.goto(0,270)
        self.write(align="center", arg=f"Score: {self.score}", font=("Courier", 20, "normal"))
    def add_score(self):
        self.score += 1
        self.clear()
        self.write(align="center", arg=f"Score: {self.score}",font=("Courier", 20, "normal"))
    def gameover(self):
        self.home()
        self.write(align="center", arg="Gameover", font=("Courier", 20, "normal"))