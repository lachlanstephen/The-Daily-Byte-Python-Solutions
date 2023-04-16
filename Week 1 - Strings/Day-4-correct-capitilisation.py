# Given a string, return whether or not it uses capitalization correctly. A string correctly uses capitalization if all letters are capitalized, no letters are capitalized, or only the first letter is capitalized.

# Ex: Given the following strings...

# "USA", return true
# "Calvin", return true
# "compUter", return false
# "coding", return true

inputString = "theDailyByte"

def correctCapitilisation(str):
    if str.isupper() or str.islower():
        return True
    else:
        for i in range(1, len(str)):
            if str[i].isupper():
                return False
        return True

print(correctCapitilisation(inputString))