from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
r_paddle = Paddle((350, 0))
r_scoreboard = Scoreboard((175, 250))
l_paddle = Paddle((-350, 0))
l_scoreboard = Scoreboard((-175, 250))
ball = Ball()
screen.bgcolor("black")
screen.tracer(0)
screen.setup(height=600, width=800)
screen.title("Pong")
screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()
    ball.move()
    if ball.ycor() > 300 or ball.ycor() < -300:
        ball.bounce_y()
    if ball.distance(r_paddle) < 30 and ball.xcor() > 320:
        ball.bounce_x()
    
    if ball.distance(l_paddle) < 30 and ball.xcor() < -320:
        ball.bounce_x()
    
    if ball.xcor() > 360:
        l_scoreboard.adding()
        ball.srodek()
    elif ball.xcor() < -360:
        r_scoreboard.adding()
        ball.srodek()
screen.exitonclick()
