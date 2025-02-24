import turtle 
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# ---Click for coordination---

# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)

# turtle.mainloop()

FONT = ("Courier", 24, "normal")

class Statename(turtle.Turtle):
     def __init__(self):
        super().__init__()
        self.name = index.state
        self.x = index.x
        self.y = index.y
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(self.x, self.y)
        self.write(self.name, align="center", font=FONT)   
   

answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")
answer_state = answer_state.capitalize()

data = pandas.read_csv("50_states.csv")
# print(data)

index = (data[data.state == answer_state])
# print(index)

if index.empty:
    print("No state Found")    
else:
    print("State Found")
    Statename(index)
    



# TODO Write correct quesses on map
# TODO Use loop to allow player to keep quessing
# TODO Record the correct quesses in list
# TODO Keep track off the score


screen.exitonclick()