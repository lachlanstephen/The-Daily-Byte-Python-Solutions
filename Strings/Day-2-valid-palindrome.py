# Given a string, return whether or not it forms a palindrome ignoring case and non-alphabetical characters.
# Note: a palindrome is a sequence of characters that reads the same forwards and backwards.

# Ex: Given the following strings...

# "level", return true
# "algorithm", return false
# "A man, a plan, a canal: Panama.", return true

import re

inputString = "A man, a plan, a canal: Panama."

def validPalindrome(str):
    result = re.sub("[\W_]+", "", str)
    return result.lower() == result.lower()[::-1]

print(validPalindrome(inputString))