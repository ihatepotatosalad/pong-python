from turtle import Turtle
SRARTING_POSITION = [(-400, 0), (-400, -20), (-400, -40), (-400, -60)]


class Player(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.turtlesize(5, .20)
        self.color('white')
        self.shape('square')
        self.goto(position)

    def up(self):
        new_y = self.ycor()+20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor()-20
        self.goto(self.xcor(), new_y)
