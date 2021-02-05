from turtle import  Turtle,Screen
import pandas

states=pandas.read_csv('50_states.csv')

screen=Screen()
turtle=Turtle()

screen.title('USA states')

image='blank_states_img.gif'

screen.addshape(image)

turtle.shape(image)

number_of_states_found=0


while number_of_states_found<52:

    found=False
    state_name=screen.textinput(title=f"{number_of_states_found}/50 states found", prompt="What's another state's name")
    if state_name in states['state'].unique():
        number_of_states_found+=1
        found=True
    else:
        print('Not a state')

    if found:

        state_x=states[states['state'] == state_name].x
        state_y=states[states['state'] == state_name].y



        coords=(int(state_x),int(state_y))


        timmy=Turtle()
        timmy.penup()
        timmy.hideturtle()
        timmy.setposition(coords)
        timmy.write(state_name)


    screen.update()


screen.exitonclick()