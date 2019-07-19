# List Overlap
#
# Take two lists, say for example these two:
#
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#   b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#
# and write a program that returns a list that contains only the elements that are common between the lists
# (without duplicates). Make sure your program works on two lists of different sizes.
#
# Extras:
#     1) Randomly generate two lists to test this
#     2) Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)

import random

a = random.sample(range(20),random.randint(5, 20))
b = random.sample(range(20),random.randint(5, 20))
c = []
size = min(len(a), len(b))
count = 0

while count <= size:
    if a[count] in b:
        c.append(a[count])
    else:
        break
    count += 1

print(a)
print(b)
print(f"Lists a and b have the following in common\n {list(set(c))}")
