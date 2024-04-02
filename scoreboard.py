from turtle import Turtle

FONT=("Courier", 50, "bold")

class Scoreboard (Turtle):
    def __init__(self,position) :
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.score=0
        
        self.goto(position)
       
        
        
    def show_score(self):
        self.clear()
        self.write(f"{self.score}",font=FONT)
    
    def game_over(self):
        # self.goto(position)
        self.write("Game over",font=FONT)