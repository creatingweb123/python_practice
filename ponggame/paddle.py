from turtle import Turtle
WIDTH = 800
HEIGHT = 600

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=5,stretch_wid=1)
        self.setheading(90)
        self.penup()
        self.goto(position)

    def move_up(self):
        if self.ycor() < 250:
            self.forward(20)

    def move_down(self):
        if self.ycor() > -250:
           self.backward(20)

class AutoPaddle(Paddle):
    def __init__(self,position):
        super().__init__(position)
        self.go_type = 0

    def auto_move(self):
        if self.ycor() > HEIGHT/2 -60:
            self.go_type = 1
            
        elif self.ycor() < -HEIGHT/2 + 60:
            self.go_type = 0
            
        if self.go_type == 0:
            self.forward(30)
        elif self.go_type ==1:
            self.backward(30)
        