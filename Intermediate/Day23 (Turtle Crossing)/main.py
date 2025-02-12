import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing")

cars =[]
car_number = 60


player = Player()
score = Scoreboard()

screen.listen()
screen.onkey(player.turtle_move,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    
    car_number = car_number + score.level

    if car_number > 60:
        car = CarManager()
        cars.append(car)
        car_number = 0

    # Level up
    if player.ycor() > 280:
        player.goto(0, -280)
        score.level += 1
        score.update_scoreboard()

    # Cars move
    for car in cars:
        car.car_move()

        #Collision 
        if player.distance(car.xcor(),car.ycor()) < 35:
            game_is_on = False
            score.game_over()
    
        


    screen.update()

screen.exitonclick()