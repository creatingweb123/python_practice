from turtle import Screen
from paddle import Paddle, AutoPaddle
from ball import Ball
import time
import random
from scoreboard import ScoreBoard


WALL = 280
# make screen
screen = Screen()
screen.setup(width = 800, height = 600)
screen.title("Pong Game")
screen.bgcolor("black")
screen.tracer(0)
# make scoreboard
scoreboard = ScoreBoard()

# make paddle
paddle = Paddle((-350,0))
auto_paddle = Paddle((350,0)) # Autopaddle도 가능

# maked ball
random_angle = float(random.randint(0,360))
ball = Ball()


screen.listen()
# lpaddle
screen.onkeypress(fun = paddle.move_up,key = "w")
screen.onkeypress(fun = paddle.move_down,key = "s")
# rpaddle
screen.onkeypress(fun = auto_paddle.move_up,key = "Up")
screen.onkeypress(fun = auto_paddle.move_down,key = "Down")

is_game_on = True
time_divide = 0.1
while is_game_on:
    time.sleep(time_divide)
    screen.update()
    #auto_paddle.auto_move()
    ball.move()

    # check_wall
    if ball.ycor() > WALL or ball.ycor() < -WALL:
        ball.change_y()

    if ball.xcor() <-320 and ball.distance(paddle) < 50 or ball.xcor() > 320 and ball.distance(auto_paddle) < 50:
        ball.change_x()
        time_divide /= 1.5

    if ball.xcor() > 390 :
        scoreboard.change_lscore()
        scoreboard.write_score()
        ball.reset_ball()

    elif ball.xcor() < -390:
        scoreboard.change_rscore()
        scoreboard.write_score()
        ball.reset_ball()

    if scoreboard.lscore > 3 or scoreboard.rscore >3:
        scoreboard.game_over()
        is_game_on = False
        


screen.exitonclick()