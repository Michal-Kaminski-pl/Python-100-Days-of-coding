from turtle import Turtle
from turtle import Screen

timmy = Turtle()
screen = Screen()
def linia():
    for i in range(15):
        timmy.pd()
        timmy.forward(10)
        timmy.pu()
        timmy.forward(10)
        i += 1
linia()
screen.exitonclick()