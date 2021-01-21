from turtle import Turtle, Screen
import random




colors = ['red', 'yellow', 'blue', 'orange', 'green','purple']

is_on=False
screen = Screen()

screen.setup(width=500,height=400)

user_bet=screen.textinput(title='Turtle race', prompt='Which turtle is going to be triumphant? pick a color: ')
turtles=[]
if user_bet:
    is_on=True
turtles=[]




for i in range(6):

    timmy=Turtle(shape='turtle')
    timmy.speed(2)
    timmy.color(colors[i])
    timmy.penup()
    timmy.goto(-230,-130+i*60)
    turtles.append(timmy)

while is_on:

   for current_turtle in turtles:
       if current_turtle.xcor()>230:
           winner=current_turtle.pencolor()
           print(f'The {winner} turtle is the champion!!!!!')
           is_on=False


       dist = random.randint(0, 10)

       current_turtle.forward(dist)





if winner==user_bet:
    print('You won the bet')
else:
    print(f'You lost the bet, you said {user_bet} turtle is going to win, but eventually the {winner} turtle won')


screen.exitonclick()