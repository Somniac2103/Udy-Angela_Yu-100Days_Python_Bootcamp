from tkinter import *
THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self):
        self.window =Tk()
        self.window.title("Quiz Master")
        self.window.config(padx=20, pady=20)
        
        self.canvas = Canvas(width=300, height=250)
        self.canvas.grid(row=1, column=0, columnspan=2)

        self.question_text = self.canvas.create_text(150, 125,text="The question", font=('arial', 20, "italic"))

        self.score_label = Label(text="Score: 0", font=("arial", 10))
        self.score_label.grid(row= 0, column= 1)
      
        self.check_img = PhotoImage(file="./images/true.png")
        self.cross_img = PhotoImage(file="./images/false.png")

        self.true_button = Button(image=self.check_img)
        self.true_button.grid(row= 2, column= 0)

        self.false_button = Button(image=self.cross_img)
        self.false_button.grid(row= 2, column= 1)

        self.window.mainloop()