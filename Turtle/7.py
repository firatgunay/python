# spiral helix

import turtle

drawing_screen = turtle.Screen()
drawing_screen.bgcolor("black")
drawing_screen.title("turtle python")

turtle_instance = turtle.Turtle()
turtle_instance.color("blue")
turtle.speed(0)
turtle_colors = ["red","purple", "blue", "green","orange", "yellow","white"]

for i in range(15):
    turtle_instance.color(turtle_colors[i % 7])
    turtle_instance.circle(i * 10)
    turtle_instance.circle(-10 * i)
    turtle_instance.left(10)


turtle.done()