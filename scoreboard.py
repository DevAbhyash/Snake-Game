from turtle import Turtle
from food import Food
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score=int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.updateScore()
        self.hideturtle()
        self.write_highScore()

    def updateScore(self):
        self.write(f"Score : {self.score}", align="center", font=("Ariel", 24, "normal"))

    def gameOver(self):
        self.goto(0,0)
        self.write(f"GAME IS OVER!!!", align="center", font=("Ariel", 24, "normal"))


    def scoreAdd(self):
        self.score += 1
        self.clear()
        self.updateScore()

    def write_highScore(self):
        self.clear()
        self.goto(10, 200)
        self.write(f"High-Score : {self.high_score}", align="center", font=("Ariel", 24, "normal"))

    def reset(self):
        if self.score>self.high_score:
            self.high_score=self.score
            with open("data.txt",mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.write_highScore()

