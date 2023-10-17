from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# READING A TEXT FILE
# file = open("highscore.txt") # you need a file.close() after
# with open("highscore.txt") as file:
#     contents = file.read()
#     # does not require file.close()

# WRITING A TEXT FILE
# with open("highscore.txt", mode="a") as file:
#     file.write("hello!")

# WRITING A TEXT FILE WHEN DOESN'T EXIST
# with open("text.txt", mode="w") as file:
#     file.write("Hi new file!")

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Rip-off Slither.io")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.ycor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    # detect collision with tail
    for segment in snake.snake_part[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
