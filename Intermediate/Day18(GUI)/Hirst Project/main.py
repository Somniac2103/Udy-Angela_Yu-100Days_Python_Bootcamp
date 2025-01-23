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

row = 5
column = 5

circle_range = 5
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
        timmy.forward(spacer + 2*circle_range)
        timmy.left(90)
        timmy.forward(spacer)

    for j in range(int(row)):        
        number = randint(1, 29)
        selectedColor = (rgb_colors[number][0],rgb_colors[number][1],rgb_colors[number][2])
        timmy.color(selectedColor)
        timmy.pendown()
        timmy.circle(circle_range)
        timmy.penup()
        timmy.forward(spacer)
        

screen.exitonclick()



