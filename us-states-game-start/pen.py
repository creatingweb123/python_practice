from turtle import Turtle

class Pen(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

    def write_state(self,x,y,state_answer):
        self.goto(x,y)
        self.write(state_answer)
