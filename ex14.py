def removeDupsLoop(x):
    y = []
    for i in x:
        if i not in y:
            y.append(i)
    return y

def removeDupsSet(x):
    return set(x)

listContents = input("Enter a series of strings separated by a comma: ")
s = listContents.split(",")
print(s)

print(removeDupsLoop(s))
print(removeDupsSet(s))