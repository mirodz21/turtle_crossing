import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

game_over= False

while not game_over:
    time.sleep(0.1)
    screen.update()




screen.exitonclick()




