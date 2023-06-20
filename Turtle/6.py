# shrinking square

import turtle

drawing_screen = turtle.Screen()
drawing_screen.bgcolor("yellow")
drawing_screen.title("turtle python")

turtle_instance = turtle.Turtle()
turtle_instance.color("blue")

def shrinkingSquare(size):
    for i in range(4):
        turtle_instance.forward(size)
        turtle_instance.left(90)
        size -= 5


for i in range(10):
    number = 100
    shrinkingSquare(number)
    number -= 30



turtle.done()