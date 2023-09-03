import snake
from screen import screen
from turtle import Turtle
from food import Food
import time
from scoreboard import ScoreBoard
# create snake body
snake = snake.Snake(screen,Turtle)
# # make snake by food
# def make_snake():
#     snake = Turtle(shape = "square")
#     snake.color("white")
#     last_snake_pos = snake_list[-1].position()
#     snake.setpos(last_snake_pos)
#     snake_list.append(snake)

# # move the snake


# # create snake food
# def make_food():
#     food = Turtle(shape="circle")
#     food.shapesize(0.5,0.5,0.5)
#     x = random.randint(-250,250)
#     y = random.randint(-250,250)
#     food.setpos(x,y)
#     return food

is_game_on = True
food = Food(width=600,height=600)
scoreboard = ScoreBoard()

while is_game_on:
    time.sleep(0.1)
    snake.move_snake()

    if snake.main_snake.distance(food.position())<15:
        food.move()
        scoreboard.change_score()
        scoreboard.write_score()
        snake.plus_snake()
    check = snake.check_out(width=580,height=580)
    if not check:
        is_game_on = False
        scoreboard.game_over()
    

# food = make_food()
screen.exitonclick()