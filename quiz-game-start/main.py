from data import *


def _check_answer(question, choice):
    print(choice)
    if question["answer"] == choice:
        print('answer is correct!')
        return True
    else:
        print('answer is not correct!')
        return False


is_finish = False
correct_answer = 0
print('start')

for bot_question in question_data:
    print("///////////////////////////////\n")
    print(bot_question)
    user_choice = input(f"{bot_question['text']} ? (True, False): ")
    if _check_answer(bot_question, user_choice):
        correct_answer += 1
        print(f" your right answer = ({len(question_data)}:{correct_answer})")
    else:
        print(f" your right answer = ({len(question_data)}:{correct_answer})")

print("end")
