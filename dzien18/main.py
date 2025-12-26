from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape('turtle')
screen = Screen()
screen.colormode(255)
timmy.color((150, 150, 150))

def kwadrat():
    i = 0
    while i < 4:
        timmy.forward(100)
        timmy.right(90)
        i += 1
kwadrat()
screen.exitonclick()
