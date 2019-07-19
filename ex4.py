# Divisors
#
# Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
# (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example,
# 13 is a divisor of 26 because 26 / 13 has no remainder.)

dividend = int(input("Enter a number: "))
divisors = []
foo = range(1, dividend + 1)

for i in foo:
    if dividend % i == 0:
        divisors.append(i)

print(divisors)