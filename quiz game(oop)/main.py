
from quiz_question import question_bank

class quiz:
    def __init__(self,q_question, a_answer ):
        self.question = q_question
        self.answer = a_answer

    def display_question(self, question):
        print(question.question_bank)


obj = quiz
print(obj.display_question)