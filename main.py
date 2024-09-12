from turtle import Screen
from paddle import Paddle
from blocks import Block
from ball import Ball
from scoreboard import Scoreboard
import time

COLORS = ["red", "orange", "yellow", "green"]
BLOCKS = []


def init_blocks(color, round_num):
    x, y = 630, 90
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
TOTAL_SCORE = Scoreboard(position=(0, 335), color="blue", score=0)
TOTAL_LIVES = Scoreboard(position=(-620, 335), color="red", score=3)

screen.listen()
screen.onkeypress(paddle.paddle_right, "Right")
screen.onkeypress(paddle.paddle_left, "Left")

for color in COLORS:
    init_blocks(color=color, round_num=COLORS.index(color)+1)

screen.update()

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    ball.move()
    screen.update()

    for block in BLOCKS:
        if ball.distance(block) < 50:
            block.hideturtle()
            ball.bounce_y()
            TOTAL_SCORE.score += block.score
            BLOCKS.remove(block)
            screen.update()
    TOTAL_SCORE.update_score(text=f"Score: {TOTAL_SCORE.score}", size=38)
    TOTAL_LIVES.update_score(text=f"Lives: {TOTAL_LIVES.score}", size=24)

    if ball.distance(paddle) < 130 and -330 < ball.ycor() < -300:
        ball.bounce_y()

    if ball.ycor() > 390:
        ball.bounce_y()

    if ball.xcor() > 680 or ball.xcor() < -680:
        ball.bounce_x()

    if ball.ycor() < -390:
        TOTAL_LIVES.score -= 1
        time.sleep(1)
        ball.starting_pos()


screen.exitonclick()
