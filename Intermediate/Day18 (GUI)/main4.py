from turtle import Turtle, Screen
from random import randint

timmy_the_turtle = Turtle()
screen = Screen()
screen.colormode(255)


timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("green")

# random cardinal direction
timmy_the_turtle.pensize(20)
timmy_the_turtle.speed(10)
for _ in range(200):
    # direction = randint(1,4)
    timmy_the_turtle.left(90 *randint(0,3))
    # match direction:
    #     case 1:
    #         continue
            
    #     case 2:
    #         timmy_the_turtle.left(90)

    #     case 3:
    #         timmy_the_turtle.right(90)
        
    #     case 4:
    #         timmy_the_turtle.right(180)

    timmy_the_turtle.forward(50)
    timmy_the_turtle.color(randint(1, 255), randint(1, 255), randint(1, 255))

screen.exitonclick()
