import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
scoreboard = Scoreboard()
player = Player()
cars = CarManager()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.onkey(fun=player.move, key= "Up")
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.add_car()
    cars.move()
    if player.ycor() > 280:
        player.level_up()
        scoreboard.adding()
        cars.level_up()
    for car in cars.cars_list:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()