from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("green")

# for _  in range(4):
#     timmy_the_turtle.forward(300)
#     timmy_the_turtle.left(90)

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


        

screen = Screen()
screen.exitonclick()
