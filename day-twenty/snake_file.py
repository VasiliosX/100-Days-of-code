from turtle import Turtle
MOVE_DISTANCE = 20
STARTING_POSITIONS = [(0, 0),(-20, 0),(-40, 0)]
UP=90
LEFT=180
RIGHT=0
DOWN=270
class Snake:

    def __init__(self):

      self.turtles = []
      self.create_snake()
      self.head=self.turtles[0]

    def create_snake(self):
      for position in STARTING_POSITIONS:
        self.add_turtle(position)

    def add_turtle(self,position):
        timmy = Turtle(shape='square')
        timmy.color('white')
        timmy.penup()
        timmy.goto(position)
        self.turtles.append(timmy)


    def extend(self):
        self.add_turtle(self.turtles[-1].position())





    def move(self):
        for turtle_num in range(len(self.turtles)-1, 0, -1):
            new_xcor=self.turtles[turtle_num-1].xcor()
            new_ycor=self.turtles[turtle_num-1].ycor()
            self.turtles[turtle_num].goto(x=new_xcor, y=new_ycor)
        self.head.forward(MOVE_DISTANCE)


    def left(self):
        if self.head.heading()!=RIGHT:
         self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
         self.head.setheading(RIGHT)
    def up(self):
        if self.head.heading() != DOWN:
         self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
         self.head.setheading(DOWN)
