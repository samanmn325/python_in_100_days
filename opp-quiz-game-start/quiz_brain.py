import data
from question_model import Question


class Brain:
    def __init__(self):
        self.qlist = data.question_data
        self.correct_answer = 0

    def create_question_list(self):
        for question in self.qlist:
            q = Question(question['text'], question['answer'])
            chosen_answer = input(f"{q.text} ? (True, False): ")
            if q.check_answer(chosen_answer):
                self.correct_answer += 1
                print("correct")
            else:
                print("not correct")

            print(f"your right answer is {self.correct_answer} from {len(self.qlist)} \n")

