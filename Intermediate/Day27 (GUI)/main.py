from tkinter import *

window = Tk()
window.title("My First Gui Program")
window.minsize(width=500, height=300)

# label

my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack()

# button

def button_clicked():
    # print("I got clicked")
    my_label.config(text = input.get())

button = Button(text="Click Me", command=button_clicked)
button.pack()

# entry

input = Entry(width = 10)
input.pack()












window.mainloop()

