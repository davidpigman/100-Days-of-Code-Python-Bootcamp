

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

intUserChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))

lstChoices = [0, 1, 2]

intComChoice = random.randint(0, 2)

if intUserChoice == 0:
    strUserChoice = rock
elif intUserChoice == 1:
    strUserChoice = paper
elif intUserChoice == 2:
    strUserChoice = scissors

if intComChoice == 0:
    strComChoice = rock
elif intComChoice == 1:
    strComChoice = paper
elif intComChoice == 2:
    strComChoice = scissors

print(f"User chose {intUserChoice}\n {strUserChoice}")

print(f"Computer chose {intComChoice}\n {strComChoice}")

if intComChoice == 0:
    if intUserChoice == 0:
        strResult = "Tie"
    elif intUserChoice == 1:
        strResult = "Win"
    elif intUserChoice == 2:
        strResult = "Lose"
elif intComChoice == 1:
    if intUserChoice == 0:
        strResult = "Lose"
    elif intUserChoice == 1:
        strResult = "Tie"
    elif intUserChoice == 2:
        strResult = "Win"
elif intComChoice == 2:
    if intUserChoice == 0:
        strResult = "Win"
    elif intUserChoice == 1:
        strResult = "Lose"
    elif intUserChoice == 2:
        strResult = "Tie"

if strResult == "Win":
    print ("You Win!")
elif strResult == "Lose":
    print ("You Lose!")
elif strResult == "Tie":
    print ("Tie, Try again!")