input_value = [2, 3, -6, 1, 3, -1, 2, 4]

first_list = []
second_list = []

f = 1
s = -1
for value in input_value:
    first_list.append(value*f)
    second_list.append(value*s)
    f *=-1
    s *=-1

def find_max(e_list):
    max_value_index = 0
    max_value = -100000
    total_value = 0
    for data_index in range(len(e_list)):
        total_value += e_list[data_index]
        if total_value > max_value:
            max_value = total_value
            max_value_index = data_index
    return max_value_index, max_value
    
def find_min(e_list,max_value_index):
    min_value = 0
    total_value = 0
    for data_index in range(max_value_index):
        total_value += e_list[data_index]
        if total_value < min_value:
            min_value = total_value

    return min_value

def find_max_value(first_list):
    max_value_index, max_value = find_max(first_list)

    if not max_value_index:
        return max_value
    else:
        min_value = find_min(first_list,max_value_index)
        return max_value - min_value
    

first_value = find_max_value(first_list)
second_value = find_max_value(second_list)

print(max(first_value, second_value))