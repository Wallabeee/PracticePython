# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that
# tells them the year that they will turn 100 years old.
#
# Extras:
#     1. Add on to the previous program by asking the user for another number and printing out that many copies of
#     the previous message. (Hint: order of operations exists in Python)
#     2. Print out that many copies of the previous message on separate lines.
#     (Hint: the string "\n is the same as pressing the ENTER button)

import datetime

name = input("Enter your name: ")
age = int(input("Enter your age: "))
num1 = int(input("Enter another number: "))
now = datetime.datetime.now()
currYear = now.year

timeTo100 = 100 - age
hundYear = currYear + timeTo100

str = f"\n{name}, you will be 100 in {timeTo100} years, which is in {hundYear}."

print(str)

print(num1 * str)