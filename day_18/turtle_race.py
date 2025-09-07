import turtle
import turtle as t
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(500,400)
user_bet = screen.textinput(title="Turtle race", prompt="Place your bets, Which turtle would win the race: ?")
colors = ["red","blue","green","yellow","cyan"]
positions = [-70,-40,-10,20,50]
all_turtles = []

for turtle_index in range(0,5):
    new_turtle = t.Turtle()
    new_turtle.shape("turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x = -230, y = positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won!, winning color was {winning_color}")
            else:
                print(f"You've lost!, winning color was {winning_color}")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
