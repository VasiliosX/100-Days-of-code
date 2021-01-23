from turtle import Screen
from snake_file import Snake
import time
from food_file import Food
from scoreboard_file import Scoreboard

screen = Screen()

screen.setup(width=600,height=600)

screen.bgcolor('black')

screen.title('OFIS')
screen.tracer(0)

snake=Snake()
food=Food()
score=Scoreboard()

screen.listen()

screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')



game_is_on=True

while game_is_on:
  screen.update()
  time.sleep(0.1)
  snake.move()


  if snake.head.distance(food)<15:

    score.eat()
    food.set_random_location()
    snake.extend()

  for segments in snake.turtles[1:]:
    if snake.head.distance(segments)<8:
      score.game_over()
      game_is_on=False


  if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
    game_is_on=False
    score.game_over()

screen.exitonclick()