from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self,width,height):
        super().__init__()
        self.width = width
        self.height = height
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.color("blue")
        self.move()

    def move(self):
        x = float(random.randint(-self.width/2+20,self.width/2-20))
        y = float(random.randint(-self.height/2+20,self.height/2-20))
        self.setpos(x,y)
