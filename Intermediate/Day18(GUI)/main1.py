from turtle import Turtle, Screen
from random import randint

timmy_the_turtle = Turtle()
screen = Screen()
screen.colormode(255)


timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("green")

for _  in range(4):
    timmy_the_turtle.forward(300)
    timmy_the_turtle.left(90)


screen.exitonclick()
