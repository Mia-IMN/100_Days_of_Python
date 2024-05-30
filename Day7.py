# coding Hangman game

import random


word_list = ["ardvark", "baboon", "camel"]
print(word_list)
print("")

# Steps - 1

#TODO1 - Randomly choose a word from the word_list and assign it to a 
# variable called chosen_word

chosen_word = random.choice(word_list)

display = []
print("Guess a possible letter in this word")
for letter in chosen_word:
    display += "_"

print(display)
print("")

#TODO2 - Ask the user to guess a letter and assign their answer to a 
# variable called guess. Make guess lowercase.

guess = input("Guess a letter: ").lower()

#TODO3 - Check if the user guessed (guess) is one of the letters in 
# chosen_word

num = 0
for i in chosen_word:
    if guess == i:
        display.insert(num, i)
    num += 1

print(display)
print("")
# Step - 2

