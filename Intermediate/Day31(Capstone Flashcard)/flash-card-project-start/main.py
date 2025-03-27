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
card_front_img = PhotoImage(file="./images/card_back.png")
canvas.create_image(400, 263, image=card_front_img)
canvas.grid(row=0, column=1, columnspan=2)

window.mainloop()
