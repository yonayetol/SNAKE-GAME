from turtle import *
class blen(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.up()
the_food_list=[]
import random
class The_Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.5)
        self.up()
        self.color("red")

    def put_the_food_randomly(self):
        if len(the_food_list)==0:
            self.goto(x=random.randint(-280,280),y=random.randint(-280,280))
            the_food_list.append(self)

