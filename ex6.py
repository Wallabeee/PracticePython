# String Lists
#
# Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome
# is a string that reads the same forwards and backwards.)

palindrome = input("Enter a word: ")
a = []
b = []
c = 0

for c in palindrome:
    a.append(c)

b = list(reversed(a))

if a == b:
    print(f"{palindrome} is a palindrome!")

else:
    print(f"{palindrome} is not a palindrome!")