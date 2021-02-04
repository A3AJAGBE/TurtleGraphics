import random
import turtle

# show the screen and close on click
screen = turtle.Screen()

turtle_sample = turtle.Turtle()
turtle_sample.shape('turtle')


# turtle_sample.hideturtle()

# # Generate random RGB color
# turtle.colormode(255)
#
#
# # Generate RGB colors
# def generate_color():
#     red = random.randint(0, 255)
#     blue = random.randint(0, 255)
#     green = random.randint(0, 255)
#     color = (red, blue, green)
#     return color

"""# A sketch app
def forward():
    turtle_sample.color('#00FFFF')
    turtle_sample.forward(15)


def backward():
    turtle_sample.color('#FF1493')
    turtle_sample.backward(15)


def counter_clockwise():
    turtle_sample.color('#FFD700')
    turtle_sample.left(10)


def clockwise():
    turtle_sample.color('#556B2F')
    turtle_sample.right(10)


def clear():
    turtle_sample.reset()


screen.onkey(fun=forward, key='W')
screen.onkey(fun=backward, key='S')
screen.onkey(fun=counter_clockwise, key='A')
screen.onkey(fun=clockwise, key='D')
screen.onkey(fun=clear, key='C')
screen.listen()"""

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
screen.title('Different Shapes')
turtle_sample.pensize(5)
for size in range(3, 11):
    turtle_sample.color(generate_color())
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

"""# Draw the random walk with the generated color
screen.title('A Random Walk')
turtle_sample.pensize(10)
direction = [0, 90, 180, 270]
turtle_sample.speed('fastest')
for _ in range(150):
    turtle_sample.color(generate_color())
    turtle_sample.forward(50)
    turtle_sample.setheading(random.choice(direction))"""

"""# Draw a Spirograph
screen.title('A Spirograph')
turtle_sample.speed('fastest')
for _ in range(int(360/5)):
    turtle_sample.color(generate_color())
    turtle_sample.circle(150)
    turtle_sample.right(5)"""

screen.exitonclick()
