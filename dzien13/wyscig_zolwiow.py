from turtle import Turtle, Screen
import random

s = Screen()
s.colormode()
s.setup(width=500, height=400)
user_bet = s.textinput(title='Make your bet', prompt='ktory zolw wygra wyscig, podaj kolor?:\n')
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_start = -150
lista_zulwiuw = []
for zulw_ktury in range(0, 6):
    zulw = Turtle(shape = 'turtle')
    zulw.up()
    zulw.color(colors[zulw_ktury])
    zulw.goto(-230, y_start)
    y_start +=50
    lista_zulwiuw.append(zulw)

race_is_on = True
while race_is_on == True:
    for zulw in lista_zulwiuw:
        zulw.forward(random.randint(0, 10))
        if zulw.position()[0] > 230:
            if zulw.color()[0] == user_bet.lower():
                print(f"Wygrales wygral twoj zulw {zulw.color()[0]}!")
                race_is_on = False
            else:
                print(f"Przegrales, wygral zulw {zulw.color()[0]}")
                race_is_on = False

s.exitonclick()