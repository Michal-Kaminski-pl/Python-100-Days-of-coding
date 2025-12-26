from turtle import Screen
from snake import Snake
from food import Food
import time
from scoreboard import Scoreboard
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("My snake game")
screen.tracer(0)
screen.listen()
screen.onkey(key= 'w', fun= snake.move_up)
screen.onkey(key= 's', fun= snake.move_down)
screen.onkey(key= 'a', fun= snake.move_left)
screen.onkey(key= 'd', fun= snake.move_right)
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    for segment in snake.segments:
        if segment == snake.segments[0]:
            pass
        elif snake.segments[0].distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
    snake.move()
    
    if snake.segments[0].distance(food) <= 15:
        snake.add_segment()
        scoreboard.adding()
        food.refresh()
        for n in range(1, len(snake.segments), 1):
            if food.pos() == snake.segments[n].position():
                food.refresh()
        

    if snake.segments[0].position()[0] > 300 or snake.segments[0].position()[0] < -300 or snake.segments[0].position()[1] > 300 or snake.segments[0].position()[1] < -300:
        scoreboard.reset()
        snake.reset()

screen.exitonclick()