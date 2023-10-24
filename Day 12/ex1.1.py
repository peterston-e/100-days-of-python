# Guessing game 

from random import randint
import art

EASY_LEVEL = 10
HARD_LEVEL = 5

def check_answer(guess, answer, turns):
    """Checks answer aginst guess. returns remaing turns"""
    if guess > answer:
        print("Too high")
        return turns - 1
    elif guess < answer:
        print("Too low")
        return turns - 1
    else:
        print(f"You got it! the answer is {answer}")

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL
    elif level == "hard":
        return HARD_LEVEL

def game():
    print(art.logo)
    print("Welcome to the guessing game")
    print("I'm thinking of a number between 1 and 100")

    answer = randint(1, 100)   

    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've ran out of guesses. You lose.")
            return
        elif guess != answer:
            print("Guess again")

game()