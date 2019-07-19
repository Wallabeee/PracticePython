# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
# Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of
# numbers in the sequence to generate.(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the
# sequence is the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

def fibGen(num):
    fibNums = []
    i = 0

    while i != num:
        if i >= 2:
            num2 = i - 2
            num1 = i - 1
            newNum = fibNums[num2] + fibNums[num1]
            fibNums.append(newNum)
        else:
            fibNums.append(i)

        i += 1

    print(fibNums)

fibNum = int(input("How many Fibonacci numbers would you like to generate? "))
fibGen(fibNum)