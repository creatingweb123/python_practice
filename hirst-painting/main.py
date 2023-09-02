import colorgram
import turtle as t
import random
# def make_color_tup(image_path,color_num):
#     colors = colorgram.extract(image_path,color_num)
#     # make tup of rgb data in the list
#     color_list = list((color.rgb.r, color.rgb.g, color.rgb.b) for color in colors)
#     return color_list

# color_list = make_color_tup("hirst-painting/painting.jpg",30)[4:]
# print(color_list)
tim = t.Turtle()
tim.speed("fastest")
tim.hideturtle()
t.colormode(255)
color_list = [(139, 164, 184), (27, 114, 171), (202, 141, 167), (237, 213, 67), (219, 157, 89), (22, 136, 66), (139, 21, 37), (124, 72, 94), (185, 176, 26), (70, 30, 37), (182, 73, 41), (225, 170, 197), (52, 36, 34), (232, 83, 40), (39, 174, 99), (108, 190, 136), (9, 107, 64), (29, 169, 185), (181, 95, 112), (38, 37, 43), (239, 216, 8), (188, 184, 210), (158, 207, 215), (152, 214, 174), (240, 169, 154), (105, 41, 39)]  
y=-300
tim.penup()
for _ in range(10):
    tim.setpos(-300,y)
    for _ in range(10):
        color = random.choice(color_list)
        tim.dot(20,color)
        tim.forward(50)
    y += 50

screen = t.Screen()
screen.exitonclick()