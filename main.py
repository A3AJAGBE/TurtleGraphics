import turtle

turtle_sample = turtle.Turtle()
turtle_sample.shape('turtle')

"""# Draw a square
for i in range(4):
    turtle_sample.forward(100)
    turtle_sample.right(90)"""

# Draw a dashed line
for i in range(10):
    turtle_sample.forward(10)
    turtle_sample.penup()
    turtle_sample.forward(10)
    turtle_sample.pendown()

# show the screen and close on click
screen = turtle.Screen()
screen.exitonclick()
