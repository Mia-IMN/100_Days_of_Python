import os

print(
    """
 _____________________
|  _________________  |
| |  Mia's    Calc  | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
    """
)

def calculator_function(num1, num2, operator):
    """Calculate the value of two inputs
    based on a chosen arithmetic symbol"""
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2
    else: 
        return "Operator not recognized"

should_continue = True

while should_continue == True:
    first_num = int(input("What's the first number?: "))
    print("+\n-\n*\n/")
    operator = input("Pick an operation: ")
    second_num = int(input("What's the next number?: "))

    result = calculator_function(first_num, second_num, operator)
    print(result)

    next_operation = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
    if next_operation == "n":
        os.system('cls')
    elif next_operation == "y":
        next_operator = input("Pick an operation: ")
        next_num = int(input("What's the next number? "))
        next_result = calculator_function(result, next_num, next_operation)
        print(next_result)
