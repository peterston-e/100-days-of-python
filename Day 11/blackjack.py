from random import choice

cards = [
    11,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    10,
    10,
    10,
]


def deal(n):
    """provide the number of cards you want delt"""
    card_list = []
    for i in range(0, n):
        delt_card = choice(cards)
        card_list.append(delt_card)
    return card_list


def sum_cards(card_list):
    """function returns a sums card list but checks if > than 21 and 11 in list and converts to 1 if it is"""
    sum_of_card_list = sum(card_list)
    if sum_of_card_list > 21 and 11 in card_list:
        for i in range(0, len(card_list)):
            if card_list[i] == 11:
                card_list[i] = 1
    sum_of_card_list = sum(card_list)
    return sum_of_card_list


def print_cards():
    print(f"    your cards: {user_cards}, current score: {sum_of_user_cards}")
    print(f"    computer's first card: {computer_cards[0]}")


blackjack = True
while blackjack == True:
    want_to_play = input("Do you want to play BlackJack? type 'y' or 'n' ")
    if want_to_play == "y":
        # deal user and computer cards
        user_cards = deal(2)
        computer_cards = deal(2)
        # sum cards
        sum_of_user_cards = sum_cards(user_cards)
        sum_of_computer_cards = sum_cards(computer_cards)
        print_cards()

        # while loop control variable
        user_draws = True
        while user_draws:
            continue_play = input("Type 'y' to get another card, type 'n' to pass: ")
            if continue_play == "y":
                new_card = deal(1)
                user_cards.append(new_card[0])

                # check if its over 21
                sum_of_user_cards = sum_cards(user_cards)
                if sum_of_user_cards > 21:
                    print(
                        f"  Your final hand: {user_cards}, final score: {sum_of_user_cards}"
                    )
                    user_draws = False
                elif sum_of_user_cards <= 21:
                    print_cards()
            else:
                print(
                    f"  Your final hand: {user_cards}, final score: {sum_of_user_cards}"
                )
                user_draws = False

        # while loop control variable
        computer_draws = True
        while computer_draws:
            if sum_cards(computer_cards) < 17:
                new_card = deal(1)
                computer_cards.append(new_card[0])
            else:
                computer_draws = False

        computer_final_score = sum_cards(computer_cards)
        user_final_score = sum_cards(user_cards)
        print(
            f"  Computer's final hand: {computer_cards}, final score: {computer_final_score}"
        )

        if user_final_score > computer_final_score and user_final_score <= 21:
            print("You Win! \U0001f600")
        elif user_final_score < computer_final_score and computer_final_score <= 21:
            print("You Lose! \U0001f928")
        elif user_final_score > 21 and computer_final_score < 21:
            print("You Lose! \U0001f928")
        else:
            print("it's a Draw \U0001f643")
    else:
        print("Goodbye and good luck!")
        blackjack = False

############### Blackjack Project #####################

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

##################### Hints #####################

# Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
# Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

# Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
# Then try to create your own flowchart for the program.

# Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

# Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
# 11 is the Ace.
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
# user_cards = []
# computer_cards = []

# Hint 6: Create a function called calculate_score() that takes a List of cards as input
# and returns the score.
# Look up the sum() function to help you do this.

# Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

# Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

# Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

# Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

# Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

# Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

# Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

# Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
