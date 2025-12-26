from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.up()
        self.shape("circle")
        self.color("white")
        self.xmove = 10
        self.ymove = 10
    
    def move(self):
        new_y = self.ycor() + self.ymove
        new_x = self.xcor() + self.xmove
        self.goto(new_x, new_y)
    
    def bounce_y(self):
        self.ymove *= -1
    
    def bounce_x(self):
        self.xmove *= -1
        self.speedu_up()
    def speedu_up(self):
        self.xmove += 1
        self.ymove += 1
    def srodek(self):
        self.goto((0, 0))
        self.bounce_x()
        self.speedu_up()
