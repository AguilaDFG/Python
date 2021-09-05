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
figures = [rock, paper, scissors]
player_choice = int(input("what do you choose? Type 0 for rock, 1 for paper and 2 for scissors\n"))
computer_choice = random.randint(0,2)
if player_choice > 2 or player_choice < 0:
  print("You chose an invalid number")
else:
  print(figures[player_choice])
  print("computer chose")
  print(figures[computer_choice])
  if player_choice - computer_choice == 1:
    print("You win")
  elif player_choice == 0 and        computer_choice == 2:
    print("You win")
  elif player_choice - computer_choice == 0:
    print("Draw")
  else:
    print("You lose")