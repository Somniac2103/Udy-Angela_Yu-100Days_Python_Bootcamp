from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=200)
window.config(padx=20, pady=20)

def button_clicked():
    output = round((int(input.get())* 1.6),2)
    label_output.config(text = output)

input = Entry(width = 10)
input.grid(row=1, column=2)

label_miles = Label(text="Miles", font=("Arial", 16))
label_miles.grid(row=1, column=3)

label_text = Label(text="is equal to", font=("Arial", 16))
label_text.grid(row=2, column=1)

label_output = Label(text= 0, font=("Arial", 16))
label_output.grid(row=2, column=2)

label_km = Label(text="Km", font=("Arial", 16))
label_km.grid(row=2, column=3)

button = Button(text="Calculate", command=button_clicked)
button.grid(row=3, column=2)

window.mainloop()