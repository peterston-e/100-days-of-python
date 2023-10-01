target = int(input()) # Enter a number between 0 and 1000

even_sum = 0

for i in range(1, target + 1):
  if i % 2 == 0:
    even_sum += i

print(even_sum)