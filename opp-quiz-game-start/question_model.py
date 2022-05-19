
class Question:
    def __init__(self, question_text, answer):
        self.text = question_text
        self.answer = answer
        self.correct_answer = 0

    def check_answer(self, user_answer):
        if self.answer == user_answer:
            return True
        else:
            return False
