# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

# def greet():
#     print("hello pleased to meet you.")
#     print("I am so glad you came.")
#     print("Please, make yourself at home.")

# greet()

# Function that allows for input 
# def greet_with_name(name):
#     print(f"Hello, {name}")
#     print("How do you do?")

# greet_with_name("Dave")

# Argument is the the data you put into the function when it's called. 
# Paramiter is the variable that you build the function with.

# Functions with more than onee imput
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What's it like in {location}?")

# greet_with("Simon", "London")


# Keyword arguments
greet_with(location="Scotland", name="Kevin")

