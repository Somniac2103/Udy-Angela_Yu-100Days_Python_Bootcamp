from turtle import Turtle, Screen
from random import randint

timmy_the_turtle = Turtle()
screen = Screen()
screen.colormode(255)


timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("green")

COMPLETE = 360
sides = 2
for i in range(6):
    timmy_the_turtle.color(randint(1, 255), randint(1, 255), randint(1, 255))
    sides += 1     
    for j in range(sides):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right((COMPLETE/sides))    

screen.exitonclick()
