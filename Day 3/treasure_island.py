print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice = input("\nyou find yourself at the bank of a big river and you need to get to the other side.\nto your left is a sign that says ferry but it looks old and a sign says back in 10min.\nWill you swim across or wait? type swim or wait.\n")

if choice.lower() == "wait":
    choice = input("You made it to the other side. on the banks of the river you spot a shiney object in the tall grass. you go over to investigate and notice a skull and crossbone on a label. Do you want to pull it out or leave it alone. type: pull or leave\n")

    if choice.lower() == "leave":
        choice = input("you leave the item alone and walk along the bank of the river untill you come to a building with three doors in a row painted red yello and green respectivly. you decide to open on. which door shoudl you open? type: red, green or blue\n")
        if choice.lower() == "blue":
            print("you found the treasure. YOU WIN!")
        elif choice.lower() == "green" or "red":
            print("you die a horrible death\nGAME OVER")
        else:
            print("GAME OVER because you're an idiot")

    else:
        print("You crawl into the long grass and yank the object out and as you do it breaks open reasing a poisonous gass. you breath it in, your lungs turn to fire and you die a horrible agonising death. GAME OVER")
else:
    print("GAME OVER, you drowned!")
