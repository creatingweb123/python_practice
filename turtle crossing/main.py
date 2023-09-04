from turtle import Screen
from scoreboard import ScoreBoard
from car import CarManager
from player import Player
import time

# screen setting
screen = Screen()
screen.bgcolor("black")
screen.setup(600,600)
screen.title("Turtle Crossing")
screen.tracer(0)
# scoreboard setting
scoreboard = ScoreBoard()

# car setting
car_list = []


# player setting
player = Player()
screen.listen()
screen.onkey(key = "w", fun = player.forward_player)
screen.onkey(key = "s", fun = player.backward_player)

car_manager = CarManager()

is_game_on = True
car_n = 0
while is_game_on:
    time.sleep(0.03)
    screen.update()
    if car_n < 50: 
        car_manager.create_car()
    car_manager.move_car()
    car_manager.end_line()

    for car in car_manager.all_cars:
        if player.check_collide(car):
            scoreboard.finish_game()
            is_game_on = False

    if player.check_is_finish():
        scoreboard.add_score()
        scoreboard.write_score()
        car_manager.speed_num += 1

screen.exitonclick()