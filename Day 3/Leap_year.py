year = int(input("Which year do you want to check? "))


if year % 4 != 0:
    print("Not leap year")

elif year % 100 == 0:
    if year % 400 == 0:
        print("Leap year")

else:
    print("Leap year")

# Flow charts make this easier to plot out when things get more complicated
