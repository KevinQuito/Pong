

from turtle import Turtle
from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.goto(0, 0)
        self.new_x = 10
        self.new_y = 10
        self.move_speed = 0.1

    def move(self):   
        self.goto(self.xcor() + self.new_x, self.ycor() + self.new_y)

    def bounce(self):
        self.new_y *= -1
    
    def hit(self):
        self.new_x *= -1
        self.move_speed *= .9

    def refresh(self):
        self.hit()
        self.goto(0, 0)