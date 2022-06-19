from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.listen()

r_padddle = Paddle((350, 0))
l_padddle = Paddle((-350, 0))
ball = Ball((0, 0))
score = ScoreBoard()

screen.onkey(l_padddle.up, "w")
screen.onkey(l_padddle.down, "s")

screen.onkey(r_padddle.up, "Up")
screen.onkey(r_padddle.down, "Down")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with Paddle
    if ball.distance(r_padddle) < 50 and ball.xcor() > 320 or ball.distance(l_padddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect R paddle miss
    if ball.xcor() > 380:
        ball.reset_the_ball()
        score.l_point()

    # Detect L paddle miss
    if ball.xcor() < -380:
        ball.reset_the_ball()
        score.r_point()

screen.exitonclick()
