from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
snake = Snake()
food = Food()
screen = Screen()
scoreboard = Scoreboard()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
on = True
while on:
    screen.update()
    time.sleep((0.1))
    snake.move()
    if snake.head.distance(food) < 15:
        food.go_to_ran()
        scoreboard.add_score()
        snake.expand()
    if not -290<snake.head.xcor()<290 or not -290<snake.head.ycor()<290:
        scoreboard.reset()
        snake.reset()
    for body in snake.snake_body[1:]:
        if snake.head.distance(body) < 10:
            scoreboard.reset()
            snake.reset()
screen.exitonclick()
