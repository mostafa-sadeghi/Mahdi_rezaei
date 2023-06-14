import turtle

screen = turtle.Screen()
pen = turtle.Pen()
pen.shape('turtle')
pen.shapesize(3)
pen.color('red', 'green')
pen.pensize(3)

# pen.begin_fill()
# for i in range(3):
#     pen.forward(100)
#     pen.left(120)
# pen.end_fill()

# pen.forward(100)
# pen.backward(100)
# pen.penup()
# pen.goto(100, 100)
# pen.stamp()
# pen.pendown()
# pen.setheading(-90)
# pen.forward(200)
# pen.clear()
# pen.circle(150)
# pen2 = pen.clone()
# pen.forward(100)
# pen2.color("blue", "orange")
# pen2.forward(-100)
pen.begin_poly()
for i in range(4):
    pen.forward(100)
    pen.left(90)
pen.end_poly()
p = pen.get_poly()

screen.register_shape("m", p)
pen.shape("m")
turtle.done()
# exercise: rotated square
