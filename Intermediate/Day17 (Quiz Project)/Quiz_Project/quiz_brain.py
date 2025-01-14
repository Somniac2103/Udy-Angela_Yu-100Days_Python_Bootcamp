class QuizBrain():

    def __init__(self, list):
        self.question_number = 0
        self.question_list = list


    def next_question(self):
        answer = input("Question #" + str(self.question_number + 1) + ": " + self.question_list[self.question_number].text + " [True/False]")
        self.question_number += 1
        print(self.question_number)