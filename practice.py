import random
def input_mode():
    mode = input("If you choose the mode, then write the number of mode.\nThe mode you choose : ")

    if len(mode)>2:
        print("Can you write in number not alphabet?")
        return input_mode()
    elif int(mode)>3:
        print("There is not the mode you chose. The mode you can choose is 1, 2 or 3.")
        return input_mode()
    return mode

def print_random_bill(name, money):
    print("If total random bill is out of range, fortunately the one chosen the most expensive money will get decreased bill")
    print("But, If money is insufficient, unfortunately the one chosen the cheapest money will get increased bill")
    name_bill = []
    total_money = 0
    for i in range(len(name)):
        chosen_money = random.randint(0,money)
        name_bill.append(chosen_money)
        total_money += chosen_money
        print(f"{name[i]} is chosen ${chosen_money}")
    
    print("Let's check total bill!!!!!!!!\n")

    if total_money < money:
        cheap_person_index = name_bill.index(min(name_bill))
        name_bill[cheap_person_index] += money-total_money
        print_name_bill(name,name_bill)
    elif total_money > money:
        left_money = total_money - money
        while left_money !=0 :
            expensive_person_index = name_bill.index(max(name_bill))
            if left_money > name_bill[expensive_person_index]:
                name_bill[expensive_person_index] = 0
                left_money -= name_bill[expensive_person_index]
            elif left_money < name_bill[expensive_person_index]:
                name_bill[expensive_person_index] -= left_money
                left_money = 0
            else:
                name_bill[expensive_person_index] = 0
                left_money = 0
        print_name_bill(name,name_bill)

def print_name_bill(name, name_bill):
    for i in range(len(name)):
        print(f"{name[i]} is ${name_bill[i]}")

print("It's a BILL CHALLENGE.\nThere is three modes.\n\nOne: Russian Rullet bill.\nTwo: peaceful bill.\nThree: Random bill.\n")

mode = input_mode()
name = input("Write name of participatian. And separate with one blank : ").split(" ")
money = int(input("How much money you need to bill? Write here : $"))
if mode == "1":
    number = random.randint(0,len(name)-1)
    print(f"The one who chose to bill the money is {name[number]}")
    print(f"You should pay ${money}")
elif mode == "2":
    print(f"You guys need to bill {money/len(name)} per person")
else:
    print_random_bill(name,money)