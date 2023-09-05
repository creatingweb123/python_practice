# # file = open("my_file.txt")
# # contents = file.read() # 한줄씩 읽기
# # file.close()

# # a; append, w; write, r; reading
# with open("my_file.txt",mode="a") as file:
#     file.write("New Text.")

# # create file that do not have same same
# # with open("newnew.txt",mode="w") as file:
# #    file.write("ddddddd")

target_list = [[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]

target_list.sort(key=lambda target :target[1])

bomb_num = 0
count = 0

while count < len(target_list):
    start = target_list[count]

    last_distance = start[1]

    for target in target_list[count+1:]:
        if target[0] >= last_distance:
            break
        else:
            count += 1

    bomb_num += 1
    count += 1

print(bomb_num)
