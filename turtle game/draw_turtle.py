from turtle import Turtle, Screen, mode

tim = Turtle()
screen = Screen()
tim.setheading(90)
mode("logo")
def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def turn_right():
    tim.right(10)

def turn_left():
    tim.left(10)

def clear_turtle():
    tim.home()
    tim.clear()

screen.listen()
screen.onkeypress(key="w", fun=move_forward)
screen.onkeypress(key="s", fun=move_backward)
screen.onkeypress(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)

screen.onkey(key="c", fun=clear_turtle)

screen.exitonclick()
