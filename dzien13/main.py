from turtle import Turtle, Screen

t = Turtle()
s = Screen()
def move_up():
    t.setheading(90)
    t.forward(20)
def move_right():
    t.setheading(0)
    t.forward(20)
def move_left():
    t.setheading(180)
    t.forward(20)    
def move_down():
    t.setheading(270)
    t.forward(20)
s.listen()
s.onkey(key= 'w', fun= move_up)
s.onkey(key= 's', fun= move_down)
s.onkey(key= 'a', fun= move_left)
s.onkey(key= 'd', fun= move_right)
s.onkey(key= 'p', fun= t.pu)
s.onkey(key= 'o', fun= t.pd)
s.exitonclick()

