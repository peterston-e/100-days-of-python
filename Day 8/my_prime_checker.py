# ****************************
# It works but thee other code is much better



# Write your code below this line 👇
def prime_checker(number):
  a = 0
  if number == 2:
    print("It's a prime number.")
  elif number == 1:
    print("It's not a prime number.")
  else:
    for i in range(3, number+1):
      if number % i == 0:
        a += 1
    if a > 1:
      print("It's not a prime number.")
    else:
      print("It's a prime number.")
      


# Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input()) # Check this number
prime_checker(number=n)