from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        self.cars_list = []
        self.car_speed = STARTING_MOVE_DISTANCE
    def move(self):
        for car in self.cars_list:
            car.forward(self.car_speed)
        self.cars_list = [car for car in self.cars_list if car.xcor() > -320]
    def level_up(self):
        self.car_speed += MOVE_INCREMENT
    
    def add_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:    
            car = Turtle("square")
            car.up()
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.color(random.choice(COLORS))
            car.goto((300, random.randint(-250, 250)))
            car.setheading(180)
            self.cars_list.append(car)