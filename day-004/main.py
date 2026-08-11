# Rock Paper Scissors

import random

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

choices = [rock, paper, scissors]

player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if player < 0 or player > 2:
    print("Invalid number!")
    exit() # This ends the program
print(choices[player])

print("Computer chose:\n")
computer = random.randint(0,2)
print(choices[computer])

if player != computer:
    if player == 0:
        if computer == 2:
            print("You win!")
        if computer == 1:
            print("You lose!")
    elif player == 2:
        if computer == 1:
            print("You win!")
        if computer == 0:
            print("You lose!")
    else:
        if computer == 0:
            print("You win!")
        if computer == 2:
            print("You lose!")
else:
    print("It's a tie!")
