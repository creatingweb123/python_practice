from turtle import Turtle

STARTING_POINT = (0,-280)
MOVE_DISTANCE = 10
FINISH_LINE = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.penup()
        self.setheading(90)
        self.move_starting_point()

    def forward_player(self):
        self.forward(MOVE_DISTANCE)
    
    def backward_player(self):
        self.backward(MOVE_DISTANCE)
    
    def move_starting_point(self):
        self.goto(STARTING_POINT)

    def check_collide(self,car):
        if self.ycor() - car.ycor() > -27 and self.ycor() - car.ycor() < 27:
            if self.xcor() - car.xcor() > -23 and self.xcor() - car.xcor() < 23:
                return 1
        return 0

    def check_is_finish(self):
        if self.ycor() > FINISH_LINE:
            self.move_starting_point()
            return True
        return False