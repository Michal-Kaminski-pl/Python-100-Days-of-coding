from turtle import Turtle
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__(visible= False)
        self.up()
        self.level = 0
        self.goto((-200, 200))
        self.color("black")
        self.write(f"Level: {self.level}", align= "center", font=FONT)
    
    def adding(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", align= "center", font=FONT)
        
    def game_over(self):
        self.goto((0, 0))
        self.write("GAME OVER")