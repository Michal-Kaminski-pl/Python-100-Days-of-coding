from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.score = 0 
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.up()
        self.color("white")
        self.setpos(0, 250)
        self.write(f"Score: {self.score}. Highscore: {self.high_score}", align= "center", font=("Arial", 24, "normal"))
    
    def adding(self):
        self.score += 1
        self.update()
    
    def update(self):
        self.clear()
        self.write(f"Score: {self.score}. Highscore: {self.high_score}", align= "center", font=("Arial", 24, "normal"))
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update()
    def game_over(self):
        self.clear()
        self.write("GAME OVER", align= "center", font=("Arial", 24, "normal"))
