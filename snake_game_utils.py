from turtle import Screen, Turtle
from random import randint
def make_screen():
    myscreen = Screen()
    myscreen.setup(600, 600)
    myscreen.bgcolor("black")
    myscreen.title("Snake game")
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
