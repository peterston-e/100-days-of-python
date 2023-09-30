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

# make a grapic list of images
pictures = [rock, paper, scissors]


# put variables in a nested list for user and computer with win lose or draw
row1 = ["Draw", "Win", "Lose"]
row2 = ["Lose", "Draw", "Win"]
row3 = ["Win", "Lose", "Draw"]

possible_outcomes = [row1, row2, row3]

# get input rock, paper or scissors 0 - 2 save as var - eg 0 for rock
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(pictures[user_choice])

# generate random choice 0 - 2 save as var -  eg paper 1  comp_choice = random.randint(0, 2)
comp_choice = random.randint(0, 2)
print(f"computer chose:\n{pictures[comp_choice]}")

# index possible_outcomes - eg shoudl be computer then user (index[1][0] = lose)
outcome = possible_outcomes[comp_choice][user_choice]

# use if and print to print out if you won or not
if outcome == "Win":
  print(f"You {outcome}.")
elif outcome == "Lose":
  print(f"You {outcome}")
else:
  print(f"It's a {outcome}")