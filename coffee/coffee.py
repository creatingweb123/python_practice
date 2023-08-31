MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

class coffee_machine():
    def __init__(self, resources,profit,menu):
        self.resources = resources
        self.profit = profit
        self.menu = menu
    def report(self):
        for key, value in self.resources.items():
            print(f"{key} : {value}")
        print(f"Money : ${self.profit}")

    def check_gradient(self,coffee):
        for key, value in self.menu[coffee]["ingredients"].items():
            if self.resources[key]-value<0:
                print(f"Sorry, there is not enough {key}")
                return 0
        return 1
    def get_input(self):
        coin_list = []
        for coin in ["quarters","dimes","nickles","pennies"]:
            coin_count = int(input(f"How many {coin}?: "))
            coin_list.append(coin_count)
        return coin_list
    def check_money(self,coffee,coin_list):
        payed_money = coin_list[0]*0.25+coin_list[1]*0.1+coin_list[2]*0.05+coin_list[3]*0.01
        payed_money = round(payed_money)
        remain_money = payed_money - self.menu[coffee]["cost"]
        if remain_money >= 0:
            print(f"Here is ${remain_money} in change.")
            self.profit += payed_money
            return 1
        else:
            print("Sorry there is not enough money. Money refuned. ${payed_money}")
            return 0

    def make_coffee(self,coffee):
        for key, value in self.menu[coffee]["ingredients"].items():
            self.resources[key] -= value
        print(f"here is your {coffee}☕ Enjoy!")
                

machine = coffee_machine(resources,profit,MENU)

operate = True
while operate:
    button = input("What would you like? (espresso/latte/cappuccino): ")
    if button == "report":
        machine.report()
    elif button in machine.menu.keys():
        can_operate = machine.check_gradient(button)
        if can_operate == 1:
            coin_list = machine.get_input()
            coin_check = machine.check_money(button,coin_list)
            if coin_check == 1:
                machine.make_coffee(button)
    elif button == "stop":
        operate = False
    else:
        print("Press the correct button, please")