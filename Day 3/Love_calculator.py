
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1 = name1.lower()
name2 = name2.lower()

concat_name = name1 + name2

# print(concat_name.count('a'))
word_1 = 0
word_2 = 0

t = concat_name.count('t')
r = concat_name.count('r')
u = concat_name.count('u')
e = concat_name.count('e')

l = concat_name.count('l')
o = concat_name.count('o')
v = concat_name.count('v')
e_1 = concat_name.count('e')

word_1 = t + r + u + e
word_2 = l + o + v + e_1

print(f"score is {word_1}{word_1}")
