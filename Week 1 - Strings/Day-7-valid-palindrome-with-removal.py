# Given a string and the ability to delete at most one character, return whether or not it can form a palindrome.
# Note: a palindrome is a sequence of characters that reads the same forwards and backwards.

# Ex: Given the following strings...

# "abcba", return true
# "foobof", return true (remove the first 'o', the second 'o', or 'b')
# "abccab", return false

inputString = "abccaba"

def validPalindrome(str):
    reverseStr = str[::-1]
    if str == reverseStr:
        return True
    else:
        for i in range(len(str)):
            if str[i] != reverseStr[i]:
                str1 = str[:i] + str[i+1:]
                str2 = reverseStr[:i] + reverseStr[i+1:]
                return str1 == str1[::-1] or str2 == str2[::-1]
    
print(validPalindrome(inputString))