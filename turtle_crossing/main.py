import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player1 = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(player1.go_up,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if car.distance(player1) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player1.is_at_finish_line():
        player1.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()