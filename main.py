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

"""# Draw shapes with different sides
shape_size = [3, 4, 5, 6, 7, 8]
shape_color = ['#00FFFF', '#87CEFA', '#556B2F', '#FFD700', '#FF1493']
for size in shape_size:
    col = random.choice(shape_color)
    turtle_sample.color(col)
    for _ in range(size):
        turtle_sample.forward(100)
        turtle_sample.right(360 / size)"""

"""# Draw a random walk
turtle_sample.pensize(10)
direction = [0, 90, 180, 270]
shape_color = ['#00FFFF', '#87CEFA', '#556B2F', '#FFD700', '#FF1493']
turtle_sample.speed('fastest')
for _ in range(300):
    turtle_sample.color(random.choice(shape_color))
    turtle_sample.forward(20)
    turtle_sample.setheading(random.choice(direction))"""

# Generate random RGB color
turtle.colormode(255)


# Generate RGB colors
def generate_color():
    red = random.randint(0, 255)
    blue = random.randint(0, 255)
    green = random.randint(0, 255)
    color = (red, blue, green)
    return color


"""# Draw the random walk with the generated color
turtle_sample.pensize(10)
direction = [0, 90, 180, 270]
turtle_sample.speed('fastest')
for _ in range(300):
    turtle_sample.color(generate_color())
    turtle_sample.forward(20)
    turtle_sample.setheading(random.choice(direction))"""


# Draw a Spirograph
turtle_sample.speed('fastest')
for _ in range(int(360/5)):
    turtle_sample.color(generate_color())
    turtle_sample.circle(100)
    turtle_sample.right(5)

# show the screen and close on click
screen = turtle.Screen()
screen.exitonclick()
