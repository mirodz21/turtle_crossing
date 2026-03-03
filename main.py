import time
from turtle import Screen
from player import Player
from car_manager import Carmanager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

player = Player()
car = Carmanager()
score = Scoreboard()
screen.listen()
screen.onkey(player.move, "w")

game_over= False
while not game_over:
    time.sleep(0.1)
    screen.update()
    car.create_car() #generate cars
    car.move() #make car move

    # IF TURTLE HITS A CAR
    for i in car.all_cars:
        if player.distance(i) < 25:
            score.game_over()
            game_over= True

    # IF PLAYER GET TO THE OTHER SIDE
    if player.ycor() >= 280:
        player.game_reset()
        score.increase_score()
        car.increase_speed()

screen.exitonclick()




