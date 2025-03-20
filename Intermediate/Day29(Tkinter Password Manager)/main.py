from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

FONT_NAME = "Courier"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters_list = [choice(letters) for _ in range(randint(8, 10))]
    password_number_list = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols_list = [choice(symbols) for _ in range(randint(2, 4))]
 
    password_list = password_letters_list + password_number_list + password_symbols_list
    shuffle(password_list)

    password = "".join(password_list)

    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_input.get()
    user = user_input.get()
    password = password_input.get()

    if website and user and password:

        is_ok = messagebox.askokcancel(title=website, message= f"Check the details: \nEmail: {user} \nPassword: {password} \nIs it ok to save?")

        if is_ok:
            entry = f'${website} | ${user} | ${password}\n'
            
            with open("./passwords.txt", "a") as data:
                data.write(entry)

            # password_list = open("./passwords.txt", "a")
            # password_list.write(entry)
            # password_list.close()

            website_input.delete(0,'end')
            password_input.delete(0,'end')
    else:
        messagebox.showwarning(title="Warning!", message="All fields are required")





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

generate_button = Button(text="Generate Password", font=(FONT_NAME, 10), command=generate_password)
generate_button.grid(row= 3, column= 2)

add_button = Button(text="Add", font=(FONT_NAME, 10), width=45, command=save)
add_button.grid(row= 4, column= 1, columnspan=2)

window.mainloop()