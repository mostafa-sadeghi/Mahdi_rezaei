from turtle import Screen, Turtle
from random import randint


def make_screen():
    myscreen = Screen()
    myscreen.setup(600, 600)
    myscreen.bgcolor("black")
    myscreen.title("Snake game")
    myscreen.tracer(False)
    return myscreen


def make_turtle(tshape, tcolor):
    myturtle = Turtle()
    myturtle.shape(tshape)
    myturtle.color(tcolor)
    myturtle.penup()
    myturtle.speed("fastest")
    return myturtle


def change_food_position(snake_head):
    x = randint(-280, 280)
    y = randint(-280, 280)
    snake_head.goto(x, y)


def move_snake(head):
    if head.direction == "up":
        ypos = head.ycor()
        ypos += 20
        head.sety(ypos)
    if head.direction == "down":
        ypos = head.ycor()
        ypos -= 20
        head.sety(ypos)
    if head.direction == "right":
        xpos = head.xcor()
        xpos += 20
        head.setx(xpos)
    if head.direction == "left":
        xpos = head.xcor()
        xpos -= 20
        head.setx(xpos)


def reset(snake_head, snake_tails):
    snake_head.goto(0, 0)
    snake_head.direction = ""
    for t in snake_tails:
        t.ht()

    snake_tails.clear()
