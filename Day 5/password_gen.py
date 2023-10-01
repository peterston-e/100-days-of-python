#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# generate n random letters save in a list
password = []
for i in range(0, nr_letters):
    password.append(letters[random.randint(0, len(letters)-1 )])

# generate n random symbols save in a list
for i in range(0, nr_symbols):
    password.append(symbols[random.randint(0, len(symbols)-1 )])

# generate n random numbers save in a list
for i in range(0, nr_numbers):
    password.append(numbers[random.randint(0, len(numbers)-1 )])

for i in range(0, len(password)):
    print(password[i], end="")

print("")
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
random_password = []
copy_password = password.copy()

a = 0
for i in password:
    # generate random numbeer based on len of copy
    x = random.randint(0, len(copy_password)-1)
    # choose a random number at index of copy
    random_password.append(copy_password[x])
    copy_password.pop(x)

for i in range(0, len(random_password)):
    print(random_password[i], end="")

print("")

# could have used random.shuffle(password)
# and thene save it as string
# string_password = ""
# for char in password:
#     string_password =+ char

# print(f"Your password is: {string_password}")