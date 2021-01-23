from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 12, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.setposition(x=0,y=280)
        self.write(arg=f'Score: {self.score}', align=ALIGNMENT, font=FONT)

    def eat(self):
        self.score += 1
        self.clear()
        self.write(arg=f'Score: {self.score}', align=ALIGNMENT, font=FONT)
    def game_over(self):
        self.clear()
        self.setposition(0,0)
        self.write(arg='Game Over',align = ALIGNMENT, font = FONT)