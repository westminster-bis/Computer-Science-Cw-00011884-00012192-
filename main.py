from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


screen = Screen()  # create a new screen object
screen.setup(width=600, height=600)  # using setup method we declare screen size
screen.bgcolor("black")  # assign black as a background color
screen.title("My Snake Game")  # set a name for a window
screen.tracer(0)  # setup screen delay with a value of zero (0)

snake = Snake()  # create a new snake object
food = Food()  # create a new food object
scoreboard = Scoreboard()  # create a new scoreboard object

screen.listen()  # listen methods accept onclick methods
screen.onkey(snake.up, "Up")  # respond arrow up key, and call a function to turn the snake
screen.onkey(snake.down, "Down")  # respond arrow down key, and call a function to turn the snake
screen.onkey(snake.left, "Left")  # respond arrow left key, and call a function to turn the snake
screen.onkey(snake.right, "Right")  # respond arrow right key, and call a function to turn the snake

######### Control with W,A,S,D ##########
screen.onkey(snake.up, "w")  # respond W key, and call a function to turn the snake
screen.onkey(snake.down, "s")  # respond S key, and call a function to turn the snake
screen.onkey(snake.left, "a")  # respond A key, and call a function to turn the snake
screen.onkey(snake.right, "d")  # respond D key, and call a function to turn the snake


game_is_on = True    # set a variable to check if the game is on or not
while game_is_on:   # game is in the loop if game is not over
    screen.update()  # refresh the screen in every cycle
    time.sleep(0.1)
    snake.move()  # change the position of the snake in every cycle

    # Detect collision with food
    if snake.head.distance(food) < 20:  # if snake eats the food it
        food.refresh()                  # food position changes
        snake.extend()                  # and snake length increases
        scoreboard.increase_score()     # then add one to the score

        print("nyam nyam nyam")

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()  # if snake is touched to the edge of the screen, score is reset
        snake.reset()       # then snake length shrink down to original value

    # detect collision with tail
    for segment in snake.segments[1:]:
        if segment == snake.head:  # first segment of the snake is also his body, so we do not end game if snake goes opposite direction
            pass
        elif snake.head.distance(segment) < 10:  # if snake is touched to part of its body,
            scoreboard.reset()  # score is reset
            snake.reset()       # then snake length shrink down to original value

#### long form ####
    for segment in snake.segments:   # if snake is long enough for loop without slicing does its job
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:  # if snake head touches its body
            game_is_on = False                   # we end the game by changing variable
            scoreboard.game_over()               # and reset the score, and notify gamer that game is over


screen.exitonclick()  # dispose screen
