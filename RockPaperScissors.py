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

user_choice = int(input("What do you choose? 0 for Rock, 1 for Paper or 2 for Scissors. "))

computer_choice = random.randint(0, 2)

#1 > 0
#2 > 1
#0 > 2

print("You chose:")
if user_choice == 0:
    print(rock)
elif user_choice == 1:
    print(paper)
elif user_choice == 2:
    print(scissors)

print("Computer chose:")
if computer_choice == 0:
    print(rock)
elif computer_choice == 1:
    print(paper)
elif computer_choice == 2:
    print(scissors)

if computer_choice == user_choice:
    print("A draw!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")
elif computer_choice == 1 and user_choice == 0:
    print("You lose!")
elif computer_choice == 2 and user_choice == 1:
    print("You lose!")
else:
    print("You win!")
