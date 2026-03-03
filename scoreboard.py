from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-220,250)
        self.show_score()

    def show_score(self):
        self.write(f"Level: {self.score}",False,"center",("Courier", 15,"bold"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.show_score()

    def game_over(self):
        self.goto(0,0)
        self.color("red")
        self.write("Game Over",False,"center",("Courier", 15,"bold"))
