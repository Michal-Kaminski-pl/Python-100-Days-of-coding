from turtle import Turtle

starting_position = [(20, 0), (0,0), (-20, 0)]

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in starting_position:
            waz = Turtle(shape = 'square')
            waz.goto(position)
            waz.color("white")
            waz.up()
            self.segments.append(waz)
    
    def move_up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)
         

    def move_right(self):
        if self.segments[0].heading() != 180:  
            self.segments[0].setheading(0)

    def move_left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def move_down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)
    
    def move(self):
        for n in range(len(self.segments) - 1, 0 , -1):
            new_x = self.segments[n-1].xcor()
            new_y = self.segments[n-1].ycor()
            self.segments[n].goto(new_x, new_y)
        self.segments[0].forward(20)
    
    def add_segment(self):
        waz = Turtle(shape = 'square')
        waz.color("white")
        waz.up()
        new_x = self.segments[-1].xcor()
        new_y = self.segments[-1].ycor()
        waz.goto((new_x, new_y))
        waz.up()
        self.segments.append(waz)
    
    def reset(self):
        for segment in self.segments:
            segment.ht()
        self.segments.clear()
        self.create_snake()