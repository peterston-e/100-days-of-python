def prime_checker(number):
    is_prime = True
    # if number = 2 for loop doesnt runn so is_prime remains true. 
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number")

n = int(input("give me a number to check\n"))
prime_checker(n)