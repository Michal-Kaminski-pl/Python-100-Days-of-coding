from turtle import Turtle
from turtle import Screen
from random import randint

timmy = Turtle()
screen = Screen()
screen.colormode(255)
timmy.pensize(10)
timmy.speed(10)
def rysowanie():
    for n in range(3, 10):
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        timmy.pencolor(r, g, b)
        for i in range(n):
            timmy.forward(100)
            timmy.right(360 / n)
            i += 1
        n += 1

rysowanie()
screen.exitonclick()