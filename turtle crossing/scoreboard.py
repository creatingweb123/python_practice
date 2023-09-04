from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(-280,260)
        self.score = 0
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(arg=f"SCORE: {self.score}",align="left",font=("Arial",20,"normal"))

    def add_score(self):
        self.score +=1

    def finish_game(self):
        self.goto(0,0)
        self.write(arg="YOU LOSE THIS GAME!!!",align="center",font=("Arial",35,"normal"))