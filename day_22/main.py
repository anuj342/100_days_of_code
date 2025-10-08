from turtle import Turtle, Screen
from paddle import Paddle

screen = Screen()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.setup(800, 600)
screen.title("Ping pong")
screen.bgcolor("black")
screen.tracer(0)

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()
