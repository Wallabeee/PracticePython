# Odd or Even
#
# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message
# to the user. Hint: how does an even / odd number react differently when divided by 2?
#
# Extras:
#     1) If the number is a multiple of 4, print out a different message.
#     2) Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
#     If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

print("\nThis program will determine if a number is even or odd.")
num = int(input("Enter a number: "))
check = int(input("Enter a second number: "))

if num % check == 0:
    print(f"{check} divides evenly into {num}.")

else:
    print(num, "Does not divide evenly by", check)

if num % 4 == 0:
    print(f"{num} is a multiple of 4 and is even.")

elif num % 2 == 0:
    print(f"{num} is even.")

else:
    print(f"{num} is odd.")