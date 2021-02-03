import random
import turtle

turtle_sample = turtle.Turtle()
turtle_sample.shape('turtle')

"""# Draw a square
for i in range(4):
    turtle_sample.forward(100)
    turtle_sample.right(90)"""

"""# Draw a dashed line
for i in range(10):
    turtle_sample.forward(10)
    turtle_sample.penup()
    turtle_sample.forward(10)
    turtle_sample.pendown()"""

# Draw shapes with different sides
shape_size = [3, 4, 5, 6, 7, 8]
shape_color = ['#00FFFF', '#87CEFA', '#556B2F', '#FFD700', '#FF1493']
for size in shape_size:
    col = random.choice(shape_color)
    turtle_sample.color(col)
    for _ in range(size):
        turtle_sample.forward(100)
        turtle_sample.right(360 / size)


# show the screen and close on click
screen = turtle.Screen()
screen.exitonclick()
