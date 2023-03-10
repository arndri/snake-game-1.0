from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from score import Board

Screen = Screen()
Screen.setup(width=600,height=600)
Screen.bgcolor("black")
Screen.title("Snake Game")
Screen.tracer(0)

snake = Snake()
food = Food()
score_board = Board()

Screen.listen()
Screen.onkey(snake.up,"Up")
Screen.onkey(snake.down,"Down")
Screen.onkey(snake.left,"Left")
Screen.onkey(snake.right,"Right")

game_on = True
while game_on:
    Screen.update()
    time.sleep(0.1)
    snake.move()

    #Deteksi head dengan food
    if snake.head.distance(food)<15:
        snake.extend()
        food.pindah()
        score_board.tambah()

    #Deteksi head dengan wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        Screen.clear()
        score_board.akhir()
        game_on = False

    #Deteksi head dengan tail
    for segment in snake.segment[1:]:
        if snake.head.distance(segment) < 10 :
            game_on = False
            Screen.clear()
            score_board.akhir()

Screen.exitonclick()