from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
<<<<<<< HEAD
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()
    def update_scoreboard(self):
        self.clear()
        self.goto(0,300)
        self.write(f"{self.l_score} - {self.r_score}", align="center", font=("Courier", 20, "normal"))
    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()
    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()
=======
        self.score1 = 0
        self.score2 = 0
        self.ht()
        self.pu()
        self.speed(0)
        self.color("white")
        self.goto(0,370)
        self.write(align="center", arg=f"{self.score1} - {self.score2}", font=("Courier", 20, "normal"))
    def add_score1(self):
        self.score1 += 1
        self.clear()
        self.write(align="center", arg=f"Score: {self.score1} - {self.score2}",font=("Courier", 20, "normal"))
    def add_score2(self):
        self.score2 += 1
        self.clear()
        self.write(align="center", arg=f"Score: {self.score1} - {self.score2}",font=("Courier", 20, "normal"))
>>>>>>> day 22
