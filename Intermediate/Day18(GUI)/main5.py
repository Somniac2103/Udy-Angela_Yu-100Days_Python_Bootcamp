from turtle import Turtle, Screen
from random import randint

timmy_the_turtle = Turtle()
screen = Screen()
screen.colormode(255)


timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("green")
# timmy_the_turtle.color(randint(1, 255), randint(1, 255), randint(1, 255))
timmy_the_turtle.pensize(1)
timmy_the_turtle.speed(0)

CIRCLE = 360
offset = 12
circle_range = 100

for _ in range(int(CIRCLE/offset)):
    timmy_the_turtle.circle(circle_range)
    timmy_the_turtle.left(offset)

screen.exitonclick()
