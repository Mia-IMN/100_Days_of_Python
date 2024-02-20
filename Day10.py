

print(
    """"
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
    """"
)


while should_continue == True
    first_num = int(input("What's the first number?: "))
    print("+\n-\n*\n\\\n")
    operator = input("Pick an operation: ")
    next_num = int(input("What's the next number?: "))

    

    next_operation = input("Type 'y' to continue calculating with 10.0, or type 'n' to start a new calculation: ")
    if next_operation == 'n':
        should_continue == False
