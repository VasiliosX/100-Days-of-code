import turtle as t
import colorgram
import random
import numpy as np




#colors=colorgram.extract('10hirst1-superJumbo.jpg',12)

#colors_list=[]

#for c in colors:
#    colors_list.append(tuple(c.rgb))




#del colors_list[0:3]

#print(colors_list)


colors_list = [(234, 166, 59), (45, 112, 157), (113, 150, 203), (212, 123, 164), (16, 128, 96), (172, 44, 88), (1, 177, 143), (153, 18, 54), (224, 201, 117)]

t.colormode(255)

timmy = t.Turtle()


timmy.shape('turtle')

screen = t.Screen()
timmy.penup()


for j in range(10):

    timmy.penup()
    timmy.setx(-200)
    timmy.sety(-200+50*j)

    for _ in range(10):

        color=random.choice(colors_list)
        timmy.dot(20,color)

        timmy.forward(50)





screen.exitonclick()