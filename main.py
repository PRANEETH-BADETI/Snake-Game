from turtle import Turtle,Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

myscreen = Screen()
myscreen.setup(width=600, height=600)
myscreen.bgcolor("black")
myscreen.title("My Snake Game")
myscreen.tracer(0)

mysnake = Snake()
food = Food()
score = Scoreboard()

myscreen.listen()
myscreen.onkey(fun=mysnake.up, key="w")
myscreen.onkey(fun=mysnake.down, key="s")
myscreen.onkey(fun=mysnake.left, key="a")
myscreen.onkey(fun=mysnake.right, key="d")

game_on = True
while game_on:
    myscreen.update()
    time.sleep(0.12)
    mysnake.move()

    #detect collision with food
    if mysnake.head.distance(food)<15:
        food.refresh()
        mysnake.extend()
        score.score_update()

    #detect collision with wall
    if mysnake.head.xcor()>280 or mysnake.head.xcor()<-280 or mysnake.head.ycor()>280 or mysnake.head.ycor()<-280 :
        game_on = False

    #detect collision with tail
    for segment in mysnake.segments[1:]:
        if mysnake.head.distance(segment)<10:
            game_on = False

    if not game_on:
        score.game_over()

myscreen.exitonclick()

