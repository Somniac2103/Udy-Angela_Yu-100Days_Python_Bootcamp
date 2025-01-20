from turtle import Turtle, Screen
from random import randint

timmy_the_turtle = Turtle()
screen = Screen()
screen.colormode(255)


timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("green")

# for _  in range(4):
#     timmy_the_turtle.forward(300)
#     timmy_the_turtle.left(90)

# for steps in range(50):
#     for _ in range(5):
#         timmy_the_turtle.penup()
#         timmy_the_turtle.forward(2)
#         timmy_the_turtle.pendown()
#         timmy_the_turtle.forward(2)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.pendown()
#     timmy_the_turtle.forward(10)


# COMPLETE = 360
# sides = 2
# for i in range(6):
#     timmy_the_turtle.color(randint(1, 255), randint(1, 255), randint(1, 255))
#     sides += 1     
#     for j in range(sides):
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right((COMPLETE/sides))    


# random cardinal direction
for _ in range(1000):
    direction = randint(1,4)
    case direction:
    
# color change
# thicker line
# draw quicker


screen.exitonclick()
