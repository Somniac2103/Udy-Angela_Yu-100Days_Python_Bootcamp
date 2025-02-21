import turtle

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

answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")

# TODO Convert to Title case
# TODO Check guess with 50 states
# TODO Write correct quesses on map
# TODO Use loop to allow player to keep quessing
# TODO Record the correct quesses in list
# TODO Keep track off the score


screen.exitonclick()