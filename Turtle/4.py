# drawing star

import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("yellow")
drawing_board.title("python turtle")

star = turtle.Turtle()

for i in range(5):
    star.right(144)
    star.forward(200)
    

turtle.done()