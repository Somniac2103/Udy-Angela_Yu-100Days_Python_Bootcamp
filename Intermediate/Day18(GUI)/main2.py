from turtle import Turtle, Screen
from random import randint

timmy_the_turtle = Turtle()
screen = Screen()
screen.colormode(255)


timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("green")

for steps in range(50):
    for _ in range(5):
        timmy_the_turtle.penup()
        timmy_the_turtle.forward(2)
        timmy_the_turtle.pendown()
        timmy_the_turtle.forward(2)
    timmy_the_turtle.penup()
    timmy_the_turtle.forward(10)
    timmy_the_turtle.pendown()
    timmy_the_turtle.forward(10)

screen.exitonclick()
