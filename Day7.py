# coding Hangman game

import random

# Steps

#TODO1 - Randomly choose a word from the word_list and assign it to a 
# variable called chosen_word

#TODO2 - Ask the user to guess a letter and assign their answer to a 
# variable called guess. Make guess lowercase.

#TODO3 - Check if the user guessed (guess) is one of the letters in 
# chosen_word

word_list = ["ardvark", "baboon", "camel"]

guess = input("Guess a letter: ")

chosen_number = random.choice(word_list)

chosen_word = word_list[chosen_number]

print (chosen_number)

print(chosen_word)

for i in chosen_word:
    if guess == i:
        print ("True")
    else:
        print ("False")

