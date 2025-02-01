from snake import Snake
from food import Food
from score import Board
from rl_agent import DQNAgent
import numpy as np
import time
from turtle import Screen

# Set up screen
Screen = Screen()
Screen.setup(width=600, height=600)
Screen.bgcolor("black")
Screen.title("Snake Game AI")
Screen.tracer(0)

# Initialize objects
snake = Snake()
food = Food()
score_board = Board()

# RL Agent
state_size = 6  # Snake position, food position, direction, obstacles
action_size = 4  # Up, Down, Left, Right
agent = DQNAgent(state_size, action_size)
batch_size = 32

# Game Loop
game_on = True
while game_on:
    Screen.update()
    time.sleep(0.1)

    # Get state
    state = np.array([
        snake.head.xcor(), snake.head.ycor(),
        food.xcor(), food.ycor(),
        int(snake.head.xcor() > 290 or snake.head.xcor() < -290 or 
            snake.head.ycor() > 290 or snake.head.ycor() < -290),
        int(any(snake.head.distance(segment) < 10 for segment in snake.segment[1:]))
    ])

    # Choose action
    action = agent.act(state)
    if action == 0:
        snake.up()
    elif action == 1:
        snake.down()
    elif action == 2:
        snake.left()
    elif action == 3:
        snake.right()

    # Move Snake
    snake.move()

    # Check rewards
    reward = -1  # Default small penalty
    done = False

    # Food collision
    if snake.head.distance(food) < 15:
        reward = 10
        snake.extend()
        food.pindah()
        score_board.tambah()

    # Wall or self-collision
    if state[4] or state[5]:
        reward = -10
        done = True
        score_board.akhir()

    # Store experience and train agent
    next_state = np.array([
        snake.head.xcor(), snake.head.ycor(),
        food.xcor(), food.ycor(),
        int(snake.head.xcor() > 290 or snake.head.xcor() < -290 or 
            snake.head.ycor() > 290 or snake.head.ycor() < -290),
        int(any(snake.head.distance(segment) < 10 for segment in snake.segment[1:]))
    ])

    agent.remember(state, action, reward, next_state, done)
    agent.replay(batch_size)

    if done:
        game_on = False

Screen.exitonclick()
