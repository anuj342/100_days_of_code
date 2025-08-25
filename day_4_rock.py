paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)"""

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)"""

scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)"""

import random

game_images = [rock, paper, scissor]

user_input = int(input("""Choose 
                   1. Rock 
                   2. Paper 
                   3. Scissor
                   """))

print("You chose: ")
if user_input >= 0 and user_input <= 2:
    print(game_images[user_input])

computer_choice = random.randint(0, 2)

print("Computer choose: ")
print(game_images[computer_choice])

if user_input == computer_choice:
    print("It's a draw!")
elif (user_input == 0 and computer_choice == 2) or \
     (user_input == 1 and computer_choice == 0) or \
     (user_input == 2 and computer_choice == 1):
    print("You win!")
else:
    print("Computer wins!")
    
