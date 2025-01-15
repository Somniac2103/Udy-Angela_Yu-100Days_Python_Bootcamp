class QuizBrain:

    def __init__(self, list):
        self.question_number = 0
        self.question_list = list

    def still_has_questions(self):
        return self.question_number < len(self.question_list)    
    
    def next_question(self):
        current_question = self.question_list[self.question_number]
        answer = input(f"Question #" + str(self.question_number + 1) + ": " + self.question_list[self.question_number].text + " [True/False]")
        self.question_number += 1

    