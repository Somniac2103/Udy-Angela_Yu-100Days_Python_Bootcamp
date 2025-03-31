from tkinter import *
from tkinter import messagebox
from random import *
import pandas
import random
import json

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- FUNCTIONS ------------------------------ # 
error_message_dict = {}
# load data
def load_data():
    try:
        data = pandas.read_csv("./data/french_words.csv")
        print(data)
    except FileNotFoundError:
       error_message_dict["datafile"] = "No Data file found or unable to load."
       print(error_message_dict)
    else:       
        langauge_dict = {row.French: row.English for (index, row) in data.iterrows()}
        print(langauge_dict)       
        selected_french_word, selected_english_word = random.choice(list(langauge_dict.items()))
        print(selected_french_word)
        print(selected_english_word)






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
right_button = Button(image=check_image, highlightthickness=0, bd = 0, command=load_data)
right_button.grid(row=2, column=1)

cross_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=cross_image, highlightthickness=0, bd = 0, command=load_data)
wrong_button.grid(row=2, column=2)

window.mainloop()


