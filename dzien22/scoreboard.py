from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__(visible= False)
        self.up()
        self.score = 0
        self.goto(position)
        self.color("white")
        self.write(f"{self.score}", align= "center", font=("Arial", 24, "normal"))
    
    def adding(self):
        self.score += 1
        self.clear()
        self.write(f"{self.score}", align= "center", font=("Arial", 24, "normal"))
        