import turtle
import random

tim = turtle.Turtle()
screen = turtle.Screen()

tim.speed(2)
# tim.shape("turtle")
# tim.color('green')

""" to create square """
# for _ in range(4):
#     tim.forward(100)
#     tim.left(90)
""" draw a dashed line """
# for _ in range(5):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

""" create shape list square , pentagon , hexagon , ... """
# color_list = ["red", "blue", "green", "yellow", "black","purple", "grey", "orange", "brown", ]
#
#
# def drawing(num_angle):
#     angle = 360 / num_angle
#     for _ in range(num_angle):
#         tim.left(angle)
#         tim.color(random.choice(color_list))
#         tim.pensize(5)
#         tim.forward(100)
#
#
# for _ in range(3, 11):
#     drawing(_)
""" random walk """
direction = [0, 90, 180, 270, ]
turtle.colormode(255)
def choice_color():
    r = random.randint(1,255)
    g = random.randint(1,255)
    b = random.randint(1,255)
    tim.pencolor(r,g,b)
tim.pensize(4)
for _ in range(200):
    choice_color()
    tim.forward(20)
    tim.setheading(random.choice(direction))
screen.exitonclick()
