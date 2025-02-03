from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 16, 'bold')

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()        
        self.color("white")
        self.score = 0
        self.refresh_score()

    def game_over(self):
        self.goto(0, 0 )
        self.write("GAME OVER", True, align= ALIGNMENT, font= FONT)     

    
    def update_score(self):
        self.score += 1
        self.refresh_score()

    def refresh_score(self):
        self.clear()
        self.goto(10, 270)
        self.write(("Score: " + str(self.score)), True, align= ALIGNMENT, font= FONT)

       
        