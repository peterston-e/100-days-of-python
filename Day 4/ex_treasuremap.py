# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

# convert input to a list
# save each list item as a int variable
list_of_coordinates = int(position[0]), int(position[1])
pos_1 = list_of_coordinates[0] - 1
pos_2 = list_of_coordinates[1] - 1


# use the variables to refrence map variable and update it
print(pos_1)
print(pos_2)
map[pos_2][pos_1] = "X"


#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")