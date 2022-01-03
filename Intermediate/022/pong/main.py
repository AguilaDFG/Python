from turtle import Screen
<<<<<<< HEAD
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from time import sleep
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=800)
screen.title("Pong")
screen.tracer(0)
r_paddle = Paddle((380, 0))
l_paddle = Paddle((-380, 0))
ball = Ball()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
game_is_on = True
while game_is_on:
    screen.update()
    sleep(0.1)
    ball.move()
    if ball.distance(r_paddle)<25 and ball.xcor()>320 or ball.distance(l_paddle)<25 and ball.xcor()<-320:
        ball.bounce()
    if ball.xcor() > 380:
        ball.goto(0,0)
        scoreboard.l_point()
        sleep(0.5)
    if ball.xcor() < -380:
        ball.goto(0,0)
        scoreboard.r_point()
        sleep(0.5)
=======
import time
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)
ball = Ball()
paddle1 = Paddle(1)
paddle2 = Paddle(2)
paddles = [paddle1, paddle2]
scoreboard = Scoreboard()
screen.listen()
screen.onkey(paddle2.up, "Up")
screen.onkey(paddle1.up, "w")
screen.onkey(paddle2.down, "Down")
screen.onkey(paddle1.down, "s")
on = True
while on:
    screen.update()
    time.sleep(0.1)
    ball.move()
    for pad in paddles:
        pad.move()
        if pad.distance(ball)<30:
            ball.bounce()
    if ball.xcor()>390:
        scoreboard.add_score1()
        ball.goto(0, 0)
        paddle1.goto(-390, 0)
        paddle2.goto(390, 0)
    if ball.xcor()<-390:
        scoreboard.add_score2()
        ball.goto(0, 0)
        paddle1.goto(-390, 0)
        paddle2.goto(390, 0)
>>>>>>> day 22
screen.exitonclick()