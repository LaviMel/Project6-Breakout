from turtle import Screen
from paddle import Paddle
from blocks import Block
from ball import Ball
import time

COLORS = ["red", "orange", "yellow", "green"]
BLOCKS = []


def init_blocks(color, round_num):
    x, y = 630, 140
    for i in range(12):
        position = (x - (i * 115), y + (round_num * 55))
        block = Block(color=color, score=round_num * 2, position=position)
        BLOCKS.append(block)


screen = Screen()
screen.setup(height=800, width=1400)
screen.title("Breakout!")
screen.bgcolor("black")
screen.tracer(0)

paddle = Paddle()
ball = Ball()
screen.listen()
screen.onkeypress(paddle.paddle_right, "Right")
screen.onkeypress(paddle.paddle_left, "Left")

for color in COLORS:
    init_blocks(color=color, round_num=COLORS.index(color)+1)

TOTAL_SCORE = 0
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    ball.move()
    screen.update()

    screen.tracer(0)
    for block in BLOCKS:
        if ball.distance(block) < 20 and ball.ycor() < 390:
            block.hideturtle()
            ball.bounce_y()
            TOTAL_SCORE += block.score
            screen.update()

    if ball.distance(paddle) < 130 and -330 < ball.ycor() < -300:
        ball.bounce_y()

    if ball.xcor() > 680 or ball.xcor() < -680:
        ball.bounce_x()

    if ball.ycor() < -390 or ball.ycor() > 390:
        time.sleep(1)
        ball.starting_pos()


screen.exitonclick()
