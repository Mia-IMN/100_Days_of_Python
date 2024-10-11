
machine_power = True

report = {
    "Water": 300,
    "Milk": 200,
    "Coffee": 100,
    "Money": 0
}


def run_machine(): 
    global machine_power


    user_input = input("What would you like? (espresso/latte/cappuccino): ")

    def make_coffee(coffee_type):

        print("Please insert coins.")

        money_quater = int(input("How many quarters?: "))
        money_quater *= 0.25
        money_dime = int(input("How many dimes?: "))
        money_dime *= 0.10
        money_nickle = int(input("How many nickles?: "))
        money_nickle *= 0.05
        money_penny = int(input("How many pennies?: "))
        money_penny *= 0.01

        coin = money_quater + money_dime + money_nickle + money_penny

        if coffee_type == "espresso":
            if coin > 1.50:
                coin -= 1.50
                report["Coffee"] -= 18
                report["Water"] -= 50
                report["Money"] += 1.50
                print(f"Here's your {input}... Enjoy")
            if report["Coffee"] > 18:
                report["Coffee"] -= 18
            else:
                print("Sorry, there is not enough coffee")
                return
            if report["Water"] > 50:
                report["Water"] -= 50
            else:
                print("Sorry, there is not enough Water")
                return
            if coin > 1.50:
                coin -= 1.50
                report["Money"] += 1.50
                print(f"Here's {round(coin - 1.50, 2)} in change")
            else:
                print("Sorry, that's not enough money. Money refunded")
                return
            print(f"Here's your {coffee_type}... Enjoy")
        if coffee_type == "latte":
            if report["Coffee"] > 24:
                report["Coffee"] -= 24
            else:
                print("Sorry, there is not enough coffee")
                return
            if report["Water"] > 200:
                report["Water"] -= 200
            else:
                print("Sorry, there is not enough Water")
                return
            if report["Milk"] > 150:
                report["Milk"] -= 150
            else:
                print("Sorry, there is not enough Milk")
                return
            if coin > 2.50:
                coin -= 2.50
                report["Money"] += 2.50
                print(f"Here's {round(coin - 2.50, 2)} in change")
            else:
                print("Sorry, that's not enough money. Money refunded")
                return
            print(f"Here's your {coffee_type}... Enjoy")
        if coffee_type == "cappuccino":
            if report["Coffee"] > 24:
                report["Coffee"] -= 24
            else:
                print("Sorry, there is not enough coffee")
                return
            if report["Water"] > 250:
                report["Water"] -= 250
            else:
                print("Sorry, there is not enough Water")
                return
            if report["Milk"] > 100:
                report["Milk"] -= 100
            else:
                print("Sorry, there is not enough Milk")
                return
            if coin > 3.00:
                coin -= 3
                report["Money"] += 3.00
                print(f"Here's {round(coin - 3.00, 2)} in change")
            else:
                print("Sorry, that's not enough money. Money refunded")
                return
            print(f"Here's your {coffee_type}... Enjoy")
    
    if user_input == "off":
        machine_power = False
        return
    elif user_input == "report":
        print(f"Water: {report['Water']}ml\nMilk: {report['Milk']}ml\nCoffee: {report['Coffee']}g\nMoney: ${report['Money']}")
        return
    elif user_input == "espresso":
        make_coffee("espresso")
    elif user_input == "latte":
        make_coffee("latte")
    elif user_input == "cappuccino":
        make_coffee("cappuccino")
    else: 
        print("Invalid input")


while machine_power == True:
    run_machine()