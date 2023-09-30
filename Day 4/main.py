import random
import my_module

# randint(A, B) random module
# modules are chunks of functions and code
#


random_interger = random.randint(1, 4)
print(random_interger)

# imported from other file
# this is how random is imported too
print(my_module.pi)

random_float = random.random()
print(random_float)

# make one between 0 and five my solution
print(random_float + random_interger)

# class solution
print(random_float * 5)

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")
