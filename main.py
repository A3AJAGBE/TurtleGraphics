from turtle import Turtle, Screen

turtle_sample = Turtle()
turtle_sample.shape('turtle')

# Draw a square
for i in range(4):
    turtle_sample.forward(100)
    turtle_sample.right(90)

# show the screen and close on click
screen = Screen()
screen.exitonclick()
