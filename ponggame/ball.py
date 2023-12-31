from turtle import Turtle

WALL = 280

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = -10
        self.y_move = 10

    def move(self):
        new_x = self.xcor()+ self.x_move
        new_y = self.ycor()+ self.y_move
        self.goto(new_x,new_y)

    def change_y(self):
        self.y_move *= -1

    def change_x(self):
        self.x_move *= -1

    def reset_ball(self):
        self.goto(0,0)
        self.change_x()
            
            