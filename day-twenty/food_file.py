from turtle import Turtle
import random

class Food(Turtle):


    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('blue')
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.speed('fastest')
        self.set_random_location()
    def set_random_location(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)