from turtle import Screen
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

screen.listen()
# screen.onkey(snake.up,"Up")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)


screen.exitonclick()