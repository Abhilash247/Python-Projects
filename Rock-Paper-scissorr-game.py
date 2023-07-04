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

choice = [rock, paper, scissors]

your_choice = choice[int(input("What would you choose? O for rock, 1 for paper or 2 for  scissors\n"))]

computer_choice = choice[random.randint(0,2)]

print(f"You choose:{your_choice}")
print(f"Computer choose:{computer_choice}")

if your_choice == computer_choice:
  print("Its a tie")

elif your_choice == rock:
    if computer_choice == scissors:
        print("You Won")
    elif computer_choice == paper:
        print("You loose")

elif your_choice == paper:
    if computer_choice == scissors:
        print("You loose")
    elif computer_choice == rock:
        print("You loose")
      
elif your_choice == scissors:
    if computer_choice == rock:
        print("You loose")
    elif computer_choice == paper:
        print("You Won")
else:
  print("You entered the invalid number")