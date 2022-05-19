import random

import colorgram
import turtle as tur
color_list = []
colors = colorgram.extract('image.jpg.jpg', 30)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    color_list.append(new_color)

print(color_list)
color_list2 = [(223, 138, 62), (196, 145, 171), (234, 226, 204), (224, 234, 230), (142, 178, 203), (139, 82, 105), (208, 90, 69), (237, 225, 233), (188, 80, 120), (69, 105, 90), (133, 182, 135), (133, 133, 74), (64, 156, 92), (47, 156, 193), (183, 192, 201), (213, 177, 191), (19, 58, 92), (20, 68, 113), (113, 123, 149), (227, 174, 166), (172, 203, 183), (156, 206, 217), (69, 58, 47), (72, 64, 53), (111, 46, 59), (53, 70, 64)]

tur.colormode(255)
mil = tur.Turtle()
scn = tur.Screen()
mil.hideturtle()
mil.penup()
mil.speed('fastest')
mil.setheading(215)
mil.forward(300)
mil.setheading(0)

for num in range(1,100+1):
    mil.dot(15, random.choice(color_list2))
    mil.forward(50)
    if num % 10 == 0 :
        mil.setheading(90)
        mil.forward(50)
        mil.setheading(180)
        mil.forward(500)
        mil.setheading(360)



scn.exitonclick()
