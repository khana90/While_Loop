#Step 1 

word_list = ["ardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
import random
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
chosen_word = random.choice(word_list)
print(f'the solution is {chosen_word}')

display =[]
for _ in range(len(chosen_word)):
    display += "_"
print(display)

end_of_game = False

while not end_of_game:
  guess = input("Guess a letter: ").lower()
  
  for position in range(word_length):
      letter = chosen_word[position]
      print(f"Current position: {position}
      \n Current letter: {letter} \n 
      Guessed letter: {guess}")
    if letter == guess:
      display[position] = letter
    
  print (display)
  if "_" not in display:
    end_of_game = True
    print("You win.")