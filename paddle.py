from turtle import Turtle


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, -330)
        self.setheading(90)
        self.shapesize(stretch_wid=9, stretch_len=0.7)
        self.shape("square")
        self.color("#8be8f1")

    def paddle_right(self):
        if self.xcor() < 590:
            self.setx(self.xcor() + 20)

    def paddle_left(self):
        if -610 < self.xcor():
            self.setx(self.xcor() - 20)
