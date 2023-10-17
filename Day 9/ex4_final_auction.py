# import some function to clear terminal
import os
# make an empty dictionary
name_and_bids = {}

# define function for adding users to a dictionary


def add_bid(name, bid):
    name_and_bids[name] = bid


auction = True
while auction == True:
    # ask user for their name and bid
    user_name = input("what is your name\n")
    user_bid = int(input("what is your bid\n£ "))

    # put in dictionary or list maybe
    add_bid(name=user_name, bid=user_bid)

    # ask if theree are any more bidders y or n
    any_more_bidders = input("are there any more bidders? Type yes or no\n")

    # if yes run add_function again but clear the screen
    if any_more_bidders == "no":
        auction = False
    else:
        os.system("clear")


# loop through the dictionary and find the keyvalue pair with the highest bid
highest_bid = 0
name_of_bidder = ""
for name in name_and_bids:
    if name_and_bids[name] > highest_bid:
        name_of_bidder = name
        highest_bid = name_and_bids[name]


os.system("clear")
# print the winner is {name} with a bid of {bid}
print(f"the winner is {name_of_bidder} with a bid of £{highest_bid}")


# reset the system / might want to to type clear instead
# os.system("reset")
