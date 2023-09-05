import turtle
from pen import Pen

screen = turtle.Screen()
screen.title("U.S States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
check_answer = True
with open("50_states.csv") as state_file:
    state_data = state_file.readlines()

state_list = []
x_y_list = []
i=1
for datas in state_data:
    if i:
        i=0
        continue
    data = datas.strip('\n').split(',')
    state_list.append(data[0])
    x = int(data[1])
    y = int(data[2])
    x_y_list.append([x,y])

pen = Pen()
answer_state = []
while check_answer:
    state_answer = screen.textinput(title=f"Guess the state {len(answer_state)}:50",prompt= "what's another state's name").title()
    if state_answer == "Exit":
        check_answer = False

    if state_answer in state_list:
        answer_state.append(state_answer)
        state_index = state_list.index(state_answer)
        pen.write_state(x=x_y_list[state_index][0],y=x_y_list[state_index][1],state_answer=state_answer)


wrong_state_data = {"state":[]}

for data_set_index in range(len(state_list)):
    if state_list[data_set_index] not in answer_state:
        wrong_state_data["state"].append(state_list[data_set_index])

print(wrong_state_data["state"])

#screen.exitonclick()


