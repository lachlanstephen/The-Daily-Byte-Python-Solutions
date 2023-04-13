# Given a string, reverse all of its characters and return the resulting string.

# Ex: Given the following strings...

# “Cat”, return “taC”
# “The Daily Byte”, return "etyB yliaD ehT”
# “civic”, return “civic”


#TO USE A RANDOM STRING INPUI

# import random, string

# letters = string.ascii_lowercase

# inputString = "".join(random.choice(letters) for i in range(10000000))

inputString = "The Daily Byte"


# My Solution

def reverseString(str):
    newString = ""
    for i in range(len(str) - 1, -1, -1):
        newString += (str[i])
    return newString

#print(reverseString(inputString))


# Using slice

def reverseStringSlice(str):
    str = str[::-1]
    return str

print(reverseStringSlice(inputString))
