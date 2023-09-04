from turtle import Turtle
from random import choice, randint

COLOR = ["red","orange","yellow","green","blue","purple"]
CAR_YSPON = [-230, 260]
CAR_XSPON = [300, 600]
INCREASE_SPEED = 3

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.speed_num = 3
    def create_car(self):
        random_chance = randint(1,6)
        if random_chance == 6:
            new_car = Turtle()
            new_car.shape("square")
            new_car.color(choice(COLOR))
            new_car.penup()
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            self.random_y = randint(-250,250)
            new_car.goto(300,self.random_y)
            self.all_cars.append(new_car)
        
    def move_car(self):
        for car in self.all_cars:
            car.backward(self.speed_num)

    def end_line(self):
        for car in self.all_cars:
            if car.xcor()==-320:
                car.goto(300,self.random_y)

    def move_next_level(self):
        self.speed_num += INCREASE_SPEED

    # def car_start_point(self):
    #     self.goto(randrange(CAR_XSPON[0],CAR_XSPON[1]),randrange(CAR_YSPON[0],CAR_YSPON[1],20))