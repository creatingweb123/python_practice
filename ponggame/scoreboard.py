from turtle import Turtle

FONT = ("Arial",50,"normal")
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.lscore = 0
        self.rscore = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.write_score()

    def write_score(self):
        self.clear()
        self.goto(-100,220)
        self.write(self.lscore,align="center",font=FONT)
        self.goto(100,220)
        self.write(self.rscore,align="center",font=FONT)
    
    def change_rscore(self):
        self.rscore += 1

    def change_lscore(self):
        self.lscore +=1

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER, {self.lscore}:{self.rscore}",False,align="center",font=FONT)