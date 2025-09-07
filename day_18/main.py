# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract(', 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
import random
import turtle as t
from turtle import Turtle, Screen
t.colormode(255)

tom = t.Turtle()
screen = Screen()
color_list = [(222, 232, 226), (208, 160, 82), (54, 89, 131), (146, 91, 40), (140, 26, 48), (222, 206, 108), (132, 177, 203), (158, 45, 83), (47, 55, 103), (167, 160, 38), (128, 189, 143), (84, 20, 44), (36, 42, 70), (187, 93, 105), (187, 139, 170), (84, 123, 181), (59, 39, 31), (78, 153, 165), (88, 157, 91), (195, 79, 72), (45, 74, 78), (161, 202, 220), (80, 73, 44), (57, 131, 121), (218, 176, 188), (220, 183, 166), (166, 207, 165)]
tom.speed("fastest")
tom.penup()
num_of_dots = 100
tom.shape("turtle")

tom.setheading(225)
tom.forward(300)
tom.setheading(0)

for num_of_dots in range(1, num_of_dots + 1):
    tom.dot(20, random.choice(color_list))
    tom.forward(50)

    if num_of_dots % 10 == 0:
        tom.setheading(90)
        tom.forward(50)
        tom.setheading(180)
        tom.forward(500)
        tom.setheading(0)

screen.exitonclick()