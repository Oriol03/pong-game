from turtle import Turtle
import random
class Ball (Turtle):
    def __init__(self) :
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.dist_y=10
        self.dist_x=10
        self.move_speed=0.08
        
    def move(self):
        new_x=self.xcor() + self.dist_x
        new_y=self.ycor()+self.dist_y
        self.goto(new_x,new_y)
    
    def bounce_y (self):
        self.dist_y*=(-1)
    def bounce_x(self):
        self.dist_x*=-1
        self.move_speed*=0.9
        
    def restart_game(self):
        self.home()
        self.move_speed=0.08
        self.bounce_x()
    