from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen= Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Ping Pong game")
screen.tracer(0)



r_paddle= Paddle(380,0)
l_paddle=Paddle(-380,0)
ball=Ball()
score_r=Scoreboard((100,230))
score_l=Scoreboard((-100,230))

screen.listen()
screen.onkey(r_paddle.up,"Up")
screen.onkey(r_paddle.down,"Down")
screen.onkey(l_paddle.up,"+")
screen.onkey(l_paddle.down,"-")

game_on=True
while game_on :
    
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    
    # Detection with a wall
    if (ball.ycor()> 280 or ball.ycor()< -280)  :
        ball.bounce_y()
        
    # Detection with paddle 
    
    if (ball.distance(l_paddle)<50 or ball.distance(r_paddle)<50) and (ball.xcor()<-350 or ball.xcor()>350):
        ball.bounce_x()
    #Detection the messing of the paddle
    if ball.xcor()> 400 :
        
        ball.restart_game()
        score_l.score+=1
    elif ball.xcor()<-400:
        
        score_r.score+=1
        ball.restart_game()
        
    difference= abs(score_l.score-score_r.score)
    if difference==3 :
        game=Scoreboard((-150,0))
        game.game_over()
        game_on=False
    score_l.show_score()
    score_r.show_score()  
        
screen.exitonclick()