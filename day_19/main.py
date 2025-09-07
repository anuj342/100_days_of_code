import turtle as t
from turtle import Turtle, Screen

tom= t.Turtle()
screen = Screen()

def forwards():
    tom.forward(10)
def backwards():
    tom.backward(10)

def left():
    tom.left(10)

def right():
    tom.right(10)

def clear():
    tom.clear()
    tom.penup()
    tom.home()
    tom.pendown()

screen.listen()
screen.onkeypress(forwards, 'w')
screen.onkeypress(backwards, 's')
screen.onkeypress(left, 'a')
screen.onkeypress(right,'d')
screen.onkey(clear,'c')

screen.exitonclick()
