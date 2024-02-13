# This is an awesome game!! I wasn't so sure I could do it but guess what? I did :) I'm so happy
# Okay! so for the actual discription, this is a rock, paper and scissors game... I'm sure you'd love it
import random

# Getting user input
user_turn = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")

# The magic begins for user's turn
if user_turn == "0":
    print('''    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)''')
elif user_turn == "1":
    print('''    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)''')
elif user_turn == "2":
    print('''    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)''')
else:
    print("Wrong input :(\nThe only accepted inputs are 0 for Rock, 1 for Paper or 2 for Scissors\n")

# The magic begins for computer's turn
if int(user_turn) <= 2:
    print("Computer chose:")

computer_turn = random.randint(0, 2)

if computer_turn == 0:
    if int(user_turn) <= 2:
        print('''    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)''')
        print("Solid rock!\n")
    else:
        print("......")

elif computer_turn == 1:
    if int(user_turn) <= 2:
        print('''    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)''')
        print("Flexible paper :)\n")
    else:
        print("......")

elif computer_turn == 2:
    if int(user_turn) <= 2:
        print('''    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)''')
        print("Sharp scissor :|)\n")
    else:
        print("......")
else:
    print("My code seems to have broken :()")

# Code for final result
if user_turn == "0" and computer_turn == 2:
    print("Rock crushes scissors!!\nYou win!\n\n")
elif user_turn == "2" and computer_turn == 1:
    print("Scissors cuts paper to pieces!!\nYou win!\n\n")
elif user_turn == "1" and computer_turn == 0:
    print("Paper somehow defeats rock!!\nYou Win!\n\n")
elif user_turn == "0" and computer_turn == 0:
    print("It's a draw :(\nGive it another go!\n\n")
elif user_turn == "2" and computer_turn == 2:
    print("It's a draw :(\nGive it another go!\n\n")
elif user_turn == "1" and computer_turn == 1:
    print("It's a draw :(!!\nGive it another go!\n\n")
elif int(user_turn) > 2:
    print("......")
else:
    print("You lost! try again?\n\n")