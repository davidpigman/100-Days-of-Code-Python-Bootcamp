import random

from hangman_art import logo
print(logo)

end_of_game = False
guessed_correctly = False
number_of_lives = 6
same_letter = True

#word_list = ["aardvark", "baboon", "camel"]

#TODO-1 = Randomly choosea word from the word_list and assign it to a varaible called chosen_word.
chosen_word = random.choice(word_list)
print(chosen_word)

#TODO-2 = Ask the user to guess a letter and assign their answer to a variable called guess.  Make guess lowercase 


#TODO-3 = Check if the letter the user guessed (guess) is one of the letters in the chosen_word.  Print "Right" if it is the right word, "Wrong" if it's not.
#letter_found = chosen_word.find(guess)
#print(letter_found)

#letter_found = chosen_word.find(guess)
#print(letter_found)
#print(len(chosen_word))

#Create blanks
hg_guess_word = []
for _ in range(len(chosen_word)):
    hg_guess_word += "_"

while end_of_game == False:
  
  #while same_letter == True:
  guess_original = input("Choose a letter. ")
  guess = guess_original.lower()
    #letter_index = hg_guess_word.index(guess) if guess in hg_guess_word else -1
    #print(f"letter_index {letter_index}")

  #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
  if guess in hg_guess_word:
      print(f"You've already guessed {guess}")
    
 #   if letter_index > -1:
 #     print(f"You already correctly chose letter {guess} dumbass")
 #   else:
 #     same_letter = False
 #     print("Hit me")

  #print(f"guess {guess}")

  #hg_guess_word = ('_' * len(chosen_word))
  #print(f"hg_guess_word {hg_guess_word}")

  #print(f"hg_guess_word {hg_guess_word}")

  print(f"chosen_word {chosen_word.find(guess)}")
  
  if chosen_word.find(guess) == -1:
    number_of_lives -= 1
    print("You guessed incorrectly. Try again!")
    if number_of_lives == 0:
      end_of_game = True
      print("You suck and you lose")
  else:
    for position, letter in enumerate(chosen_word):
      #print(f"position {position}")
      #print(f"letter {letter}")
      if letter == guess:
        #print("Right") 
        hg_guess_word[position] = letter
    print("You guessed correctly!")
  
  #blabla = hg_guess_word.index("_")
  
  blank_index = hg_guess_word.index("_") if "_" in hg_guess_word else -1
  
  
  #print(f"blabla {blabla}")
    #print(f"hg_guess_word.index {hg_guess_word.index("_")}")
    
  if blank_index == -1:
    end_of_game = True
    print("You WIN!!!")
  
  print(f"hg_guess_word {hg_guess_word}")
  print(f"number_of_lives {number_of_lives}")

#for n in range(0,len(chosen_word)):
# # letter_in_word = chosen_word[n]
#  print(letter_in_word)
#  letter_found = letter_in_word.find(guess)
#  if letter_found == 0:
#    print("Right")
#  else:
#    print("Wrong")
  