#Step 1 

word_list = ["ardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
import random
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
chosen_word = random.choice(word_list)
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
guess = input("Guess a letter: ").lower()

for letter in chosen_word:
  if letter == guess:
    print("Mached")
  else:
    print("Not matched")