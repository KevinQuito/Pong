from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong")
screen.bgcolor("black")
screen.tracer(0)


pad1 = Paddle((350, 0)) # tuple as the argument
screen.listen()
screen.onkeypress(pad1.up, "Up")
screen.onkeypress(pad1.down, "Down")

pad2 = Paddle((-350, 0)) # tuple as the argument
screen.onkeypress(pad2.up, "w")
screen.onkeypress(pad2.down, "s")

ball1 = Ball()
score = Score()

game_over = False

while game_over != True:
    time.sleep(ball1.move_speed)
    screen.update()
    ball1.move()

    #Detect collision with wall
    if ball1.ycor() > 280 or ball1.ycor() < -280:
        ball1.bounce()
    #Detect collision with paddle
    if ball1.distance(pad1) < 50 and ball1.xcor() > 340 or ball1.distance(pad2) < 50 and ball1.xcor() < -340:    
        ball1.hit()
                    # the ball is 20 pixel and the paddle is also 20 pixels, normally we would say if the distance between the two objects is less than 20, then they probably made contact
                    # but a problem occurs when the ball hits not at the center of the paddle, rather on the edge of the paddle. Hence, we put another condition, if the xaxis of the ball is
                    # greater than 340 and the distance between the ball and paddle is less than 50, then the ball would have made contact with the paddle regardless of whether it's in the center or edges
    #Detect when paddle misses
    if ball1.xcor() > 390:
        ball1.refresh()
        score.update_l()
    if ball1.xcor() < -390:
        ball1.refresh()
        score.update_r()   

screen.exitonclick()