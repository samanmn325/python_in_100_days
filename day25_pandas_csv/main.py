import pandas
import turtle

screen = turtle.Screen()
screen.title("u.s. stats quiz")
tim = turtle.Turtle()
image = "blank_states_img.gif"
screen.addshape(image)
tim.shape(image)
data = pandas.read_csv("50_states.csv")

# def get_place(x, y):
#     print(x)
#     print(y)
#
#
# screen.listen()
# screen.onscreenclick(fun=get_place)
# screen.mainloop()
times = 0
correct = 0
right_answer = []

while times < len(data.state.to_list()):
    user_answer = screen.textinput(title=f"{correct}/{len(data.state.to_list())}", prompt='enter your choice').title()

    if user_answer in data.state.to_list():
        correct += 1
        print('yes')
        right_answer.append(user_answer)
    print(right_answer)
    times += 1


maintain_answers = [item for item in data.state.to_list() if item not in right_answer]
print(maintain_answers)