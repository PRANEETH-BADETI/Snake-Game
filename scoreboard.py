from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=270)
        self.color("white")
        self.speed(0)
        self.score_refresh()

    def score_refresh(self):
        self.write(f"Score: {self.score} ", align="center", font=("Arial", 14, "normal"))

    def score_update(self):
        self.score+=1
        self.clear()
        self.score_refresh()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align="center", font=("Arial", 20, "normal"))
