from tkinter import *
FONT_NAME = "Courier"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:", font=(FONT_NAME, 10))
website_label.grid(row= 1, column= 0)

website_input = Entry(width = 60)
website_input.grid(row=1, column=1, columnspan=2)
website_input.focus()

user_label = Label(text="Email/Username:", font=(FONT_NAME, 10))
user_label.grid(row= 2, column= 0)

user_input = Entry(width = 60)
user_input.grid(row=2, column=1, columnspan=2)
user_input.insert(0, "salmon.barry1@gmail.com")

password_label = Label(text="Password:", font=(FONT_NAME, 10))
password_label.grid(row= 3, column= 0)

password_input = Entry(width = 35)
password_input.grid(row=3, column=1)

generate_button = Button(text="Generate Password", font=(FONT_NAME, 10))
generate_button.grid(row= 3, column= 2)

add_button = Button(text="Add", font=(FONT_NAME, 10), width=45)
add_button.grid(row= 4, column= 1, columnspan=2)

window.mainloop()