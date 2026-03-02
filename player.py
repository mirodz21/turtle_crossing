from turtle import Turtle

STARTING_POSITION = (0,-260)
MOVE_DISTANCE = 20
FINISH = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("blue")
        self.penup()
        self.shapesize(1.5,1.5)
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(),new_y)

    def game_reset(self):
        self.goto(STARTING_POSITION)
