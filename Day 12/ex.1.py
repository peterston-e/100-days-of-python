# Guessing game 

from random import randint
import art

def lose_life():
    life = attempts
    life -= 1
    return life



answer = randint(1, 100)
print(art.logo)

print("I'm thinking of a number between 1 and 100")

difficulty = input("choose a difficulty. Type 'easy' or 'hard': ")
attempts = 0

if difficulty == "easy":
    attempts = 10
elif difficulty == "hard":
    attempts = 5

while attempts > 0:
    print(f"you have {attempts} attempts remaining")
    guess = int(input("Make a guess: "))
    if guess == answer:
        print(f"you got it! The answer was {answer}")
        break
    elif guess > answer:
        print("Too high\nGuess again")
        attempts = lose_life()
    else:
        print("Too low\nGuess again")
        attempts = lose_life()

if attempts == 0:
    print("You ran out of guesses, you lose.")