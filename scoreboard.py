from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self, position, color, score):
        super().__init__()
        self.color(color)
        self.penup()
        self.hideturtle()
        self.score = score
        self.goto(position)

    def update_score(self, text, size):
        self.clear()
        self.write(text, align="center", font=("courier", size, "bold"))
