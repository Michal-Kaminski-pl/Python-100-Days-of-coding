from turtle import Turtle
from turtle import Screen
from random import randint
import random
def chodzenie_w_lewo():
    timmy.left(90)
    timmy.forward(20)

def chodzenie_w_prawo():
    timmy.right(90)
    timmy.forward(20)
def prosto():
    timmy.forward(20)
def tyl():
    timmy.backward(20)
def walk(kierunki):
    n = 0
    while n < 500:
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        random_color = (r, g, b)
        timmy.pencolor(random_color)
        wybrany_kierunek = random.choice(kierunki_lista)
        wybrany_kierunek()
        n += 1

timmy = Turtle()
screen = Screen()
screen.colormode(255)
timmy.pensize(10)
timmy.speed(10)
kierunki = {"forward": prosto,"tyl": tyl,"prawo:": chodzenie_w_prawo,"lewo": chodzenie_w_lewo}
kierunki_lista = list(kierunki.values())
walk(kierunki)

screen.exitonclick()