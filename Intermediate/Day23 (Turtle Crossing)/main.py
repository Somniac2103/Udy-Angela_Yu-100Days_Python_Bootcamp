import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing")

player = Player()
score = Scoreboard()
car = CarManager()

screen.listen()
screen.onkey(player.turtle_move,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)

    # Level up
    if player.ycor() > 280:
        player.goto(0, -280)
        score.level += 1
        score.update_scoreboard()

    # Cars move
    car.car_move()

    #Collision 
    if player.distance(car.xcor(),car.ycor()) < 35:
        game_is_on = False
        


    screen.update()