import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Cross")
screen.tracer(0)
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(player.move, "Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    for car in car_manager.cars:
        car.move()
        if player.distance(car) <20:
            scoreboard.gameover()
            game_is_on = False
    if random.randint(0, 100) < 15:
        car_manager.create_car(300, random.randint(-240, 280))
    if player.ycor() > 300:
        scoreboard.level_up()
        player.level_up()
screen.exitonclick()