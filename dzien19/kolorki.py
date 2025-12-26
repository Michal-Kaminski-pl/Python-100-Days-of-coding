import colorgram
from turtle import Turtle, Screen
import random

def row_up(n):
    t.goto(50, 50 + 50 * n)
    if n > 10:
        exit()
n = 1
t = Turtle()
s = Screen()
s.screensize(600, 600)
s.setworldcoordinates(0, 0, 600, 600)
s.colormode(255)
t.up()
t.speed('fastest')
t.hideturtle()
t.goto(50, 50)
colors = colorgram.extract('image.jpg', 2 ** 32)
print(colors)
colors_rgb = [] 
dots_number = 100
for color in colors:
    r = color.rgb[0]
    g = color.rgb[1]
    b = color.rgb[2]
    rgb = (r, g, b)
    colors_rgb.append(rgb)
    
for dots in range(dots_number):
    t.dot(20, random.choice(colors_rgb))
    t.forward(50)
    if t.position()[0] > 500:
        row_up(n)
        n += 1
    dots += 1

s.exitonclick()