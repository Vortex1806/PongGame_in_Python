import time
from turtle import Screen, Turtle
from scoreboard import Scoreboard
from ball import Ball
from paddle import Paddle

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0) #removes the starting animation but we need continuous work

l_paddle = Paddle((-350,0))
r_paddle = Paddle((350,0))
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

ball = Ball()
scoreboard = Scoreboard()
#hello
game_is_on = True
while game_is_on:
    time.sleep(0.06)
    ball.move()
    screen.update() # required after using the tracer function

#     detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # if ball.distance(r_paddle) < 10 or ball.distance(l_paddle) < 10: this does not work
    #     ball.bounce()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

#     detect if r_paddle misses
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset()
        scoreboard.r_point()

screen.exitonclick()