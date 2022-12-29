from turtle import Screen, Turtle
from screen import Screen_Start
from player import Player
from ball import Ball
import time


screen = Screen()
screen.tracer(0)
screen.screensize(600, 600, 'black')


play_screen = Screen_Start()

player = Player((-400, 0))
bot = Player((400, 0))
ball = Ball()

screen.listen()
screen.onkey(player.up, 'w')

screen.onkey(player.down, 's')
screen.onkey(bot.up, 'Up')

screen.onkey(bot.down, 'Down')

game_is_on = True
while game_is_on:
    time.sleep(ball.ball_speed)

    screen.update()
    ball.move_ball()

    if ball.ycor() > 350 or ball.ycor() < -300:
        ball.bounce_y()
    if ball.distance(bot) < 50 and ball.xcor() > 390 or ball.distance(player) < 50 and ball.xcor() < -390:
        ball.bounce_x()
    if ball.xcor() > 410:
        play_screen.points_player()

        ball.reset_ball()
    if ball.xcor() < -410:
        play_screen.points_bots()
        ball.reset_ball()


screen.exitonclick()
