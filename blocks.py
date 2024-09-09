from turtle import Turtle


class Block (Turtle):

    def __init__(self, position, color, score):
        super().__init__()
        self.penup()
        self.color(color)
        self.shape("square")
        self.turtlesize(stretch_wid=5, stretch_len=2)
        self.right(90)
        self.goto(position)
        self.score = score

