from turtle import Turtle

FONT = ("Arial",15,"normal")
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.setpos(0,280)
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"This is your score:{self.score}",False,align="center",font=FONT)
    
    def change_score(self):
        self.score += 1

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",False,align="center",font=FONT)