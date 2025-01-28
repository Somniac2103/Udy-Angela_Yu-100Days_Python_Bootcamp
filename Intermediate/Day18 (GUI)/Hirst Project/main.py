import colorgram
from turtle import Turtle, Screen
from random import randint

rgb_colors = []

colors = colorgram.extract('image.jpg', 30)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)
 

print(rgb_colors)

timmy = Turtle()
screen = Screen()
screen.colormode(255)

timmy.speed("fastest")
timmy.hideturtle()
timmy.penup()
timmy.setposition([250, -250])
timmy.pendown()



row = 10
column = 10

circle_range = 20
spacer = 50

for i in range(column):
    if i%2:
        timmy.penup()
        timmy.right(90)
        timmy.forward(spacer)
        timmy.right(90)
        timmy.forward(spacer)
    else:
        timmy.penup()
        timmy.left(90)
        timmy.forward(spacer)
        timmy.left(90)
        timmy.forward(spacer)

    for j in range(int(row)):        
        number = randint(1, 29)
        selectedColor = (rgb_colors[number][0],rgb_colors[number][1],rgb_colors[number][2])
        timmy.pendown()
        timmy.dot(circle_range, selectedColor)
        timmy.penup()
        timmy.forward(spacer)
        

screen.exitonclick()



