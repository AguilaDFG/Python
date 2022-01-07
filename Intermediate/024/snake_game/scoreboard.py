from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high_score.txt") as high_score:
            self.high_score = int(high_score.read())
        self.ht()
        self.pu()
        self.speed(0)
        self.color("white")
        self.goto(0,270)
        self.update_board()
    def update_board(self):
        self.clear()
        self.write(align="center", arg=f"Score: {self.score} High score: {self.high_score}", font=("Courier", 20, "normal"))
    def add_score(self):
        self.score += 1
        self.update_board()
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", mode="w") as high_score:
                high_score.write(str(self.high_score))
        self.score = 0
        self.update_board()