from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Carmanager:

    def __init__(self):
        self.all_cars = []
        self.car_speed = MOVE_DISTANCE

    def create_car(self):
        rand = random.randint(1,6)
        if rand == 1:
            car = Turtle()
            car.shape("square")
            car.shapesize(1, 2)
            car.color(random.choice(COLORS))
            car.penup()
            random_y = random.randint(-220, 220)
            car.goto(300, random_y)
            self.all_cars.append(car)

    def move(self):
        for car in self.all_cars:
            car.backward(MOVE_DISTANCE)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT
