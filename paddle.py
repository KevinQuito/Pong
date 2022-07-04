from turtle import Turtle

MOVE_DISTANCE = 20

class Paddle(Turtle):

    def __init__(self, coor):
        super().__init__()
        self.coor = coor
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(self.coor)
        
    def up(self):
        self.goto(self.coor[0], self.ycor()+MOVE_DISTANCE)
    def down(self):
        self.goto(self.coor[0], self.ycor()-MOVE_DISTANCE)