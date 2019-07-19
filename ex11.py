# Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten,
# a prime number is a number that has no divisors.). You can (and should!) use your answer to Exercise 4 to help you.
# Take this opportunity to practice using functions, described below.

def isPrime(num):
    divisors = []

    for x in range(1, num + 1):
        if num % x == 0:
            divisors.append(x)

    if num ==1:
        print(f"{num} is not a prime number.")
    elif divisors[0] == 1 and divisors[1] == num:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")

num = int(input("Enter a number: "))
isPrime(num)