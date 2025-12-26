from turtle import Turtle
from turtle import Screen
import random

timmy = Turtle()
screen = Screen()
screen.colormode(255)
timmy.speed("fastest")
timmy.pensize(1)
timmy.hideturtle()

for n in range(0, 360, 5):
    timmy.left(5)
    timmy.heading()
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    timmy.color(random_color)
    timmy.circle(100)

screen.exitonclick()