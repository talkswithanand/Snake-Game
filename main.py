from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

food = Food()
snake = Snake()
scoreboard = Scoreboard()


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_over = False
while not game_over:
    # Show the 3 squares as one entire snake
    screen.update()
    time.sleep(0.1)
    snake.move()
    # snake.snake_speed()

    # Detect collision with food, by comparing distance of 2 turtle.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.count_score()

    # Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_over = True
        scoreboard.game_over()

    # Detect collision with tail.
    for segment in snake.all_snakes[1:]:
        if snake.head.distance(segment) < 10:
            game_over = True
            scoreboard.game_over()

















screen.exitonclick()