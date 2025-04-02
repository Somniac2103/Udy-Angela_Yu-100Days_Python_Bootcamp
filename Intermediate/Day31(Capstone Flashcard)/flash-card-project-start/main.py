from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient = "records")

# ---------------------------- FUNCTIONS ------------------------------ # 
def next_card():
    current_card = random.choice(to_learn)
    window.after_cancel(fliptimer)
    # print(current_card)
    current_card["French"]
    canvas.itemconfig(canvas_img, image=card_front_img)
    canvas.itemconfig(language_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=current_card["French"], fill="black")
    window.after(3000, lambda: update_card(current_card))

def update_card(current_card):
    # print(current_card)
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")
    canvas.itemconfig(canvas_img, image=card_back_img)
    
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg= BACKGROUND_COLOR)

canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
card_back_img = PhotoImage(file="./images/card_back.png")
card_front_img = PhotoImage(file="./images/card_front.png")
canvas_img = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(row=0, column=1, columnspan=2)

language_text = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))

word_text = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))

check_image = PhotoImage(file="./images/right.png")
right_button = Button(image=check_image, highlightthickness=0, bd = 0, command=next_card)
right_button.grid(row=2, column=1)

cross_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=cross_image, highlightthickness=0, bd = 0, command=next_card)
wrong_button.grid(row=2, column=2)

fliptimer = window.after(3000, lambda: update_card())
next_card()

window.mainloop()


