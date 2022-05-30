from turtle import Screen, Turtle
from Day21_Class import Ball, Paddle, Line, Score, Wall
from time import sleep

# Create the Screen
screen = Screen()
screen.bgcolor('black')
screen.title("Pong Game")
screen.setup(width=1000, height=750)
screen.tracer(0)

# paddle = Turtle()
# paddle.color('white')
# paddle.shape('square')
# paddle.shapesize(stretch_len=1, stretch_wid=5)
# paddle.penup()
# paddle.goto(x=350, y=0)

# Create Paddle (Class in Day21_Class.py)
paddle_right = Paddle((450, 0))
paddle_left = Paddle((-450, 0))

# Create Ball (Class in Day21_Class.py)
ball = Ball()

line = Line()

wall = Wall()

name1 = screen.textinput(title="Input name", prompt="Input name of player 1: ").upper()
name2 = screen.textinput(title="Input name", prompt="Input name of player 2: ").upper()

name1_score = Score(name1, -350, 335)
name2_score = Score(name2, 350, 335)

screen.listen()

screen.onkey(paddle_right.go_up, 'Up')
screen.onkey(paddle_right.go_down, 'Down')
screen.onkey(paddle_left.go_up, 'w')
screen.onkey(paddle_left.go_down, 's')


game_is_on = True   
while game_is_on:
    sleep(0.05)
    screen.update()
    name1_score.showName()
    name2_score.showName()
    ball.move()
    ball.bounce()
    game_is_on = ball.bounceX()
    ball.bounce_Paddle(paddle_right)
    ball.bounce_Paddle(paddle_left)

if ball.xcor()>460:
    name1_score.notification_win(-350, 0)
    name2_score.notification_lost(350, 0)
else:
    name2_score.notification_win(350, 0)
    name1_score.notification_lost(-350, 0)


screen.exitonclick()