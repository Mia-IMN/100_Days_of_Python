# coding Hangman game

import random


word_list = ["ardvark", "baboon", "camel"]

# Steps - 1

#TODO1 - Randomly choose a word from the word_list and assign it to a 
# variable called chosen_word

chosen_number = random.choice(word_list)

#TODO2 - Ask the user to guess a letter and assign their answer to a 
# variable called guess. Make guess lowercase.

guess = input("Guess a letter: ").lower

#TODO3 - Check if the user guessed (guess) is one of the letters in 
# chosen_word

for i in chosen_word:
    if guess == i:
        print ("True")
    else:
        print ("False")

# Step - 2

for letter in chosen_word:
    display = '-'
    print(display)