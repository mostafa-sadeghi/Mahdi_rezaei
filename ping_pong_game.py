import turtle

window = turtle.Screen()
window.title("Ping-pong Game")
window.bgcolor("Yellow")
window.setup(width=1050, height=650)


# left paddle
left_paddle = turtle.Turtle()
left_paddle.speed("fastest")
left_paddle.color("red")
left_paddle.shape("square")
left_paddle.shapesize(stretch_wid=6, stretch_len=2)
left_paddle.penup()
left_paddle.goto(-400, 0)
# right paddle
right_paddle = turtle.Turtle()
right_paddle.speed("fastest")
right_paddle.color("blue")
right_paddle.shape("square")
right_paddle.shapesize(stretch_wid=6, stretch_len=2)
right_paddle.penup()
right_paddle.goto(400, 0)


# ball
ball = turtle.Turtle()
ball.speed("fastest")
ball.shape("circle")
ball.color("black")
ball.penup()
ball.home()
ball.dx = 5
ball.dy = -5


left_player_score = 0
right_player_score = 0

score_board = turtle.Turtle()
score_board.speed("fastest")
score_board.color("blue")
score_board.penup()
score_board.hideturtle()
score_board.goto(0, 260)
score_board.write("Left Player:0  Right player:0",
                  align="center", font=("Arial", 24, "bold"))


def paddle_L_up():
    y = left_paddle.ycor()
    y += 20
    left_paddle.sety(y)


def paddle_R_up():
    y = right_paddle.ycor()
    y += 20
    right_paddle.sety(y)


def paddle_L_down():
    y = left_paddle.ycor()
    y -= 20
    left_paddle.sety(y)


def paddle_R_down():
    y = right_paddle.ycor()
    y -= 20
    right_paddle.sety(y)


window.listen()
window.onkeypress(paddle_R_up, "Up")
window.onkeypress(paddle_L_up, "w")
window.onkeypress(paddle_R_down, "Down")
window.onkeypress(paddle_L_down, "s")

while True:
    window.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 280:
        ball.sety(280)
        ball.dy *= -1

    if ball.ycor() < -280:
        ball.sety(-280)
        ball.dy *= -1

    if ball.xcor() > 500:
        ball.home()
        left_player_score += 1
        ball.dy *= -1
        score_board.clear()
        score_board.write(f"Left Player:{left_player_score}  Right player:{right_player_score}",
                          align="center", font=("Arial", 24, "bold"))

    if ball.xcor() < -500:
        ball.goto(0, 0)
        right_player_score += 1
        ball.dy *= -1
        score_board.clear()
        score_board.write(f"Left Player:{left_player_score}  Right player:{right_player_score}",
                          align="center", font=("Arial", 24, "bold"))

    if ball.xcor() > 360 and (ball.ycor() < right_paddle.ycor()
                              + 40 and ball.ycor() > right_paddle.ycor()-40):
        ball.setx(360)
        ball.dx *= -1

    if ball.xcor() < -360 and (ball.ycor() < left_paddle.ycor()
                               + 40 and ball.ycor() > left_paddle.ycor()-40):
        ball.setx(-360)
        ball.dx *= -1
