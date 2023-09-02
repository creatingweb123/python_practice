from turtle import Turtle, Screen
import random
color_list = ["red","orange","yellow","green","blue","purple"]
def make_turtle(num):
    turtle = Turtle(shape="turtle")
    turtle.penup()
    turtle.color(color_list[num])
    turtle.goto(x=-240, y= -150+400/num_choice*num)
    turtle.speed = "fastest"
    return turtle

def win_check(color, bat):
    if bat == color:
        print(f"You win!! {color} turtle won!!")
    else:
        print(f"You lose, {color} turtle won")
screen = Screen()
num_choice = screen.numinput(title = "Choose num",prompt = "Choose the num of turtle in range 5: ")
color_choice = screen.textinput(title = "Make your bet", prompt = "Choose the turtle's color which will win the game: ")
screen.setup(width = 500, height = 400)

turtle_list = []
for i in range(int(num_choice)):
    turtle = make_turtle(i)
    turtle_list.append(turtle)

if color_choice:
    game_check = True

while game_check:
    for t in turtle_list:
        t.forward(random.randint(0,10))
        x = t.xcor()
        if x > 230:
            game_check = False
            win_check(color=t.pencolor(),bat=color_choice)
            break




screen.exitonclick()