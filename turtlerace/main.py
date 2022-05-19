import turtle
import random
screen = turtle.Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="make your bet",prompt="which turtle will win the race? enter a color: ")
list_color = ["red",'yellow','blue','green','grey','purple','brown']
y_positions = [-70, -40, -10, 20, 50, 80]
turtle_list = []
for turtle_index in range(0, 6):
    tim = turtle.Turtle(shape="turtle")
    tim.color(list_color[turtle_index])
    tim.penup()
    tim.goto(x=-230, y=y_positions[turtle_index])
    turtle_list.append(tim)
is_finish = True
while is_finish:
    for tur in turtle_list:
        rand = random.randint(0, 10)
        tur.forward(rand)
        if tur.xcor() > 220:
            is_finish = False
            if tur.color() == user_bet:
                print('you win')
            else:
                print(f"you lose . {tur.color()} turtle wins")

screen.exitonclick()
