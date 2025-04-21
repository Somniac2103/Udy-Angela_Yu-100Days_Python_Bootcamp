from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window =Tk()
        self.window.title("Quiz Master")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        self.canvas = Canvas(width=300, height=250)
        self.canvas.grid(row=1, column=0, columnspan=2,pady=50)

        self.question_text = self.canvas.create_text(150, 125, width=280,text="The question", font=('arial', 20, "italic"), fill=THEME_COLOR)

        self.score_label = Label(text="Score: 0", font=("arial", 10), fg="white", bg=THEME_COLOR)
        self.score_label.grid(row= 0, column= 1)
      
        check_img = PhotoImage(file="./images/true.png")
        cross_img = PhotoImage(file="./images/false.png")

        self.true_button = Button(image=check_img, highlightthickness=0, command=self.send_true_answer)
        self.true_button.grid(row= 2, column= 0)

        self.false_button = Button(image=cross_img, highlightthickness=0, command=self.send_false_answer)
        self.false_button.grid(row= 2, column= 1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():            
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
        
    def send_true_answer(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def send_false_answer(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
        


