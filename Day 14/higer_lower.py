# Import random module or maybe just .chose()
from random import choice
from art import logo, vs
from game_data import data
import os

def compair(list):
    """Takes a list of 2 random accouunts in data. returns True if user guesses correctly and False if incorect"""
    a = list[0]['follower_count']
    b = list[1]['follower_count']

    choice = input("Who has more followers? Type 'A' or 'B': ").upper()

    if choice == "A" and a > b:
        return True
    elif choice == "B" and b > a:
        return True
    else:
        return False

def swap(list):
    """swaps list index 1 with index 0 and generates new random item in position index 1. returns new list"""
    list[0] = list[1]
    list[1] = choice(data)
    return list

# define the game() 
def game():
    score = 0
    # while loop
    while True:
        # create empty list to store two dicts in
        rand_list = []
        # populate the list with random dict (people) from data
        for _ in range(0, 2):
            rand_list.append(choice(data))
        # check if both items are the same 
        if rand_list[0] == rand_list[1]:
            while rand_list[0] == rand_list[1]:
                rand_list[1] = choice(data)

        # ********** uncoment line below for testing ****************
        # print(f"count A = {rand_list[0]['follower_count']}... count B = {rand_list[1]['follower_count']}")

        # print the name and descriton of A
        print(f"Compare A: {rand_list[0]['name']}, a {rand_list[0]['description']}, from {rand_list[0]['country']}.")

        # print vs askii
        print(vs)

        # print the name and description of B
        print(f"Against B: {rand_list[1]['name']}, a {rand_list[1]['description']}, from {rand_list[1]['country']}.")

        if not compair(rand_list):
            print(os.system("clear"))
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}.")
            return
        else:
            print(os.system("clear"))
            print(logo)
            score += 1
            print(f"You're right! Current score: {score}.")
            rand_list = swap(rand_list)

print(os.system("reset"))
print(logo)
game()