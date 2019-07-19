# Guessing Game One
#
# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number,
# then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user
# input lessons from the very first exercise)
#
# Extras:
#     Keep the game going until the user types “exit”
#     Keep track of how many guesses the user has taken, and when the game ends, print this out.

import random

num = random.randint(1, 9)
count = 0

print("\nThis program will let you try and guess a random number correctly. Type 'exit' when you no longer wish to play.")

while True:
    ans = input("Guess a number between 1 and 9: ")

    if ans is 'exit':
        quit()

    while int(ans) != num:
        count += 1
        if int(ans) > num:
            print("Too high!")
        elif int(ans) < num:
            print("Too low!")

        ans = input("Enter a new number: ")

    count += 1
    print(f"Exactly right! It took you {count} attempts. \nTime for another game.\n")
    count = 0