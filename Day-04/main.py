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

import random

choices = [rock, paper, scissors]

player_choice = int(input("What's your choice? " \
"Type o for Rock, 1 for Paper and 2 for Scissor."))
print(choices[player_choice])

print("Computer Choice: ")

computer_choice = random.randint(0,2)
print(choices[computer_choice])

if player_choice == computer_choice:
    print("It's a draw.")
elif player_choice == 0 and computer_choice == 1:
    print("Computer wins.")
elif player_choice == 2 and computer_choice == 3:
    print("Computer wins. :) ")
elif player_choice == 3 and computer_choice == 1:
    print("Computer wins. :) ")
else:
    print("You Won!!!!")

