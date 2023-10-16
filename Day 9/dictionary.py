# dictionary
# {key: value}
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again.",
}

print(programming_dictionary["Bug"])

# adding new items
programming_dictionary["If"] = "a conditional statement"

print(programming_dictionary)

# empty dictinary
empty_dictionary = {}

# wipe existing dictionary
# programming_dictionary = {}

# Edit items
programming_dictionary["Bug"] = "an insect"

# looping (prints the keys)
for i in programming_dictionary:
    print(i)

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
