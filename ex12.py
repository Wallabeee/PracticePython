# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new
# list of only the first and last elements of the given list. For practice, write this code inside a function.

import random

series = random.sample(range(1, 101), random.randint(1, 20))

def firstLast(series):
    end = len(series) - 1

    print(series[0], series[end])

print("This program will print the first and last entry in a list.")
firstLast(series)
