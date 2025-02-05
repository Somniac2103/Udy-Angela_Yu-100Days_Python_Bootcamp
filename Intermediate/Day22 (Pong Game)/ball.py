from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(x=0, y=0)

    def update_ball(self):
        if (self.ycor() + 10) > 590:
            new_y = self.ycor() - 10
        elif (self.ycor() + 10)
        new_y = self.ycor() + 10
        new_x = self.xcor() + 10
        self.goto(new_y , new_x)

