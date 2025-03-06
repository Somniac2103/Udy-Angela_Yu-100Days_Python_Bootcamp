from tkinter import *

window = Tk()
window.title("My First Gui Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# label

my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
# my_label.place(x=100, y=200)
my_label.grid(row= 1, column= 1)

# button

def button_clicked():
    # print("I got clicked")
    my_label.config(text = input.get())

button = Button(text="Click Me", command=button_clicked)
# button.pack()
button.grid(row= 2, column= 2)

# entry

input = Entry(width = 10)
# input.pack()
input.grid(row=3, column=4)

new_button = Button(text="New Button")
new_button.grid(row=1, column=3)

window.mainloop()

