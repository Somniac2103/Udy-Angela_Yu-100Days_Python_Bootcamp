from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
screen.setup(width=500, height=500)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colours = ["purple","blue", "green", "yellow", "orange", "red"]
y_positions = [-70, -40, -10, 20, 50 , 80]

for turtle_index in range(0, 6):

    tim = Turtle(shape="turtle")
    tim.color(colours[turtle_index])
    tim.penup()
    tim.goto(x= -230, y= y_positions[turtle_index])









screen.exitonclick()
