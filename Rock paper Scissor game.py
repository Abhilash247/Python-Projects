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
images=[rock,paper,scissors]
user_choice=int(input("What would you chose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if user_choice>=3 or user_choice<=0:
  print("You entered a invalid number")
else:
  print(images[user_choice])
computer_choice=random.randint(0,2)
print("Computer choose:")
print(images[computer_choice])
if user_choice==0:
  if computer_choice==0:
    print("It's a tie")
  elif computer_choice==1:
    print("You loose")  
  elif computer_choice==2:
    print("You won")
      
if user_choice==1: 
  if computer_choice==0:
    print("You won")
  elif computer_choice==1:
    print("It's a tie")  
  elif computer_choice==2:
    print("You loose")
      
if user_choice==2:
  if computer_choice==0:
    print("You loose")
  elif computer_choice==1:
    print("You Won")  
  elif computer_choice==2:
    print("It's a tie")
    
  
    

    
  