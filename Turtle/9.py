import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("light blue")
drawing_board.title("python turtle")

turtle_instance = turtle.Turtle()

def turtle_forward():
    turtle_instance.forward(100)

def rotate_right():
    #turtle_instance.right(90)
    turtle_instance.setheading(turtle_instance.heading()-90)
def rotate_left():
    #turtle_instance.left(90)
    turtle_instance.setheading(turtle_instance.heading()+90)

def clear_screen():
    turtle_instance.clear()

def return_home():
    turtle_instance.home()

def pen_up():
    turtle_instance.penup()

def pen_down():
    turtle_instance.pendown()

drawing_board.listen()
drawing_board.onkey(fun=turtle_forward, key="space")
drawing_board.onkey(fun=rotate_right, key="Down")
drawing_board.onkey(fun=rotate_left, key="Up")
drawing_board.onkey(fun=clear_screen, key="c")
drawing_board.onkey(fun=return_home, key="h")
drawing_board.onkey(fun=pen_down, key="w")
drawing_board.onkey(fun=pen_up, key="q")

turtle.mainloop()