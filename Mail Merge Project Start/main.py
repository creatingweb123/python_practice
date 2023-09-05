#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


# 이름 불러오기

with open("/Users/user/python_practice/Mail Merge Project Start/Input/Names/invited_names.txt",mode = "r") as file:
    name_list = file.readlines()

# 기준안을 가져오고 이름대로 작성해준다.

for name in name_list:
    new_name = name.strip('\n')
    with open(f"/Users/user/python_practice/Mail Merge Project Start/Output/ReadyToSend/{new_name}.txt",mode="w") as f:

        with open("/Users/user/python_practice/Mail Merge Project Start/Input/Letters/starting_letter.txt",mode="r") as file:
            lines = file.read()
        
        new_lines = lines.replace('[name]',new_name)
        f.write(new_lines)
        