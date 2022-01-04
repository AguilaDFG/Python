from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,350)
        self.l_score = 0
        self.r_score = 0
        self.write(align="center", arg=f"Score: {self.l_score} - {self.r_score}", font=("Courier", 15, "normal"))
    def l_point(self):
        self.l_score += 1
        self.clear()
        self.write(align="center", arg=f"Score: {self.l_score} - {self.r_score}",font=("Courier", 15, "normal"))
    def r_point(self):
        self.r_score += 1
        self.clear()
        self.write(align="center", arg=f"Score: {self.l_score} - {self.r_score}",font=("Courier", 15, "normal"))