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

game_images = [rock, paper, scissors]

your_choice = -1
computer_choice = -1

while your_choice < 0 or your_choice > 2:
    your_choice = int(input("What do you choose?\n"
          "Type 0 for Rock\n"
          "Type 1 for Paper\n"
          "Type 2 for Scissors\n"))
    if your_choice < 0 or your_choice > 2:
        print("Invalid choice!\n"
              "Try again!")

computer_choice = (random.randint(0, 2))
print(f"Your choice is: {game_images[your_choice]}")
print(f"Computer's choice is: {game_images[computer_choice]}")

if ((your_choice == 0 and computer_choice == 2) or
    (your_choice == 1 and computer_choice == 0) or
    (your_choice == 2 and computer_choice == 1)):
    print("You win!")

elif your_choice == computer_choice:
    print("Draw!")

else:
    print("You lose!")