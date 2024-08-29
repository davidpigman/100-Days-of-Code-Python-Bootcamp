import random
from art import logo

#Function to set difficulty
def choose_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard' ")
    if difficulty == "hard":
        return HARD_GUESSES_INT
    else: 
        return EASY_GUESSES_INT

def guess_number():
    #Function to check users guess against another
    global NUM_OF_GUESSES
    global RANDOM_INT

    # print(f"random int {random_int}")

    print(f"You have {NUM_OF_GUESSES} attempts remaining to guess the number.")

    num_guess = int(input("Make a guess: "))

    #Track the number of turns and reduce by 1 if they get it wrong
    if num_guess == RANDOM_INT:
        print("You won.  Game over")
    elif num_guess > RANDOM_INT:
        print("Too high.\nGuess Again.")
        NUM_OF_GUESSES -= 1
    elif num_guess < RANDOM_INT:
        print("Too low.\nGuess Again.")
        NUM_OF_GUESSES -= 1

    if num_guess == RANDOM_INT:
        print("")
    elif NUM_OF_GUESSES == 0:
        print("No more guesses left, you lose!")
    else:
        #Repeat the guessing functionality if they get it wrong
        guess_number()

MAXIMUM_NUMBER = 100
RANDOM_INT = random.randrange(1, 100, 1)
EASY_GUESSES_INT = 5
HARD_GUESSES_INT = 10

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

#Function to set difficulty
#difficulty = input("Choose a difficulty. Type 'easy' or 'hard' ")
NUM_OF_GUESSES = choose_difficulty()

#Let the user guess a number
guess_number()



