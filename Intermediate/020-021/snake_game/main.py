from turtle import Screen
import time
from snake import Snake
snake = Snake()
screen = Screen()
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
screen.exitonclick()
