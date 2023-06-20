# drawing square

import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("yellow")
drawing_board.title("python turtle")

square = turtle.Turtle()

for i in range(4):
    square.forward(200)
    square.left(90)

turtle.done()