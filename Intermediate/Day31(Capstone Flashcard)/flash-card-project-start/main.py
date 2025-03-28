from tkinter import *
from tkinter import messagebox
from random import *
import json

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg= BACKGROUND_COLOR)

canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
card_back_img = PhotoImage(file="./images/card_back.png")
card_front_img = PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
canvas.grid(row=0, column=1, columnspan=2)

language_text = canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))

word_text = canvas.create_text(400, 263, text="trouve", font=("Ariel", 60, "bold"))

check_image = PhotoImage(file="./images/right.png")
right_button = Button(image=check_image, highlightthickness=0, bd = 0)
right_button.grid(row=2, column=1)

cross_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=cross_image, highlightthickness=0, bd = 0)
wrong_button.grid(row=2, column=2)





window.mainloop()


