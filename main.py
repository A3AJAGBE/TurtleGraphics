import random
import turtle

# show the screen and close on click
screen = turtle.Screen()

turtle_sample = turtle.Turtle()
turtle_sample.shape('turtle')
turtle_sample.hideturtle()

# Generate random RGB color
turtle.colormode(255)


# Generate RGB colors
def generate_color():
    red = random.randint(0, 255)
    blue = random.randint(0, 255)
    green = random.randint(0, 255)
    color = (red, blue, green)
    return color


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
