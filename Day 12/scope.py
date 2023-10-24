
enemies = 1

def increase_enemies():
    # need to add global to modify from in function 
    global enemies
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")

# avoid modifying global scope within a function
# because it makes mistakes 

# you can use return instead 

# global constansts like pi that you dont intend on changing 
# save them as uppeercase so you know not to modify them
PI = 3.14159
URL = "https://www.google.com"