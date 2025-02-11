from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid= 1, stretch_len=2)
        self.color(random.choice(COLORS))
        self.penup()
        self.goto(280, random.randint(-280, 280))
        self.setheading(180)
        self.car_speed = random.randrange(1,10)
    
    def car_move(self):
        new_x = self.xcor() - self.car_speed
        self.goto(new_x, self.ycor())