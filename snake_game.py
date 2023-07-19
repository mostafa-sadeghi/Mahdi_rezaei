from snake_game_utils import *
from time import sleep

main_surface = make_screen()
root = main_surface._root

def on_close():
    global running
    running = False

root.protocol("WM_DELETE_WINDOW",on_close)



score = 0
high_score = 0

snake_head = make_turtle("square", "blue")
snake_head.direction = ""
snake_food = make_turtle("circle", "red")
change_food_position(snake_food)

score_board = make_turtle("square", "white")
score_board.goto(0, 260)
score_board.ht()


def go_up():
    if snake_head.direction != "down":
        snake_head.direction = "up"


def go_down():
    if snake_head.direction != "up":
        snake_head.direction = "down"


def go_right():
    if snake_head.direction != "left":
        snake_head.direction = "right"


def go_left():
    if snake_head.direction != "right":
        snake_head.direction = "left"


main_surface.listen()
main_surface.onkeypress(go_up, "w")
main_surface.onkeypress(go_down, "s")
main_surface.onkeypress(go_left, "a")
main_surface.onkeypress(go_right, "d")

snake_bodies = []
running = True
while running:
    main_surface.update()
    score_board.clear()
    score_board.write(f"Score: {score}\tHighScore: {high_score}", align="center", font=("arial", 22))
    if snake_head.distance(snake_food) < 20:
        score += 1
        if score > high_score:
            high_score = score
        change_food_position(snake_food)
        new_body = make_turtle("square", "grey")
        snake_bodies.append(new_body)

    for i in range(len(snake_bodies) - 1, 0, -1):
        x = snake_bodies[i-1].xcor()
        y = snake_bodies[i-1].ycor()
        snake_bodies[i].goto(x, y)

    if len(snake_bodies) > 0:
        x = snake_head.xcor()
        y = snake_head.ycor()
        snake_bodies[0].goto(x, y)

    if snake_head.xcor() > 290 or snake_head.xcor() < -290 or snake_head.ycor() > 290 or snake_head.ycor() < -290:
        reset(snake_head, snake_bodies)
        score = 0

    move_snake(snake_head)

    for body in snake_bodies:
        if body.distance(snake_head) < 20:
            reset(snake_head, snake_bodies)
            score = 0


    sleep(0.2)
