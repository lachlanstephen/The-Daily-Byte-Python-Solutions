# Given two binary strings (strings containing only 1s and 0s) return their sum (also as a binary string).
# Note: neither binary string will contain leading 0s unless the string itself is 0

# Ex: Given the following binary strings...

# "100" + "1", return "101"
# "11" + "1", return "100"
# "1" + "0", return  "1"

binStr1 = "1011"
binStr2 = "1"

def addBinary(str1, str2):
    return str(bin(int(str1, 2) + int(str2, 2)))[2:]

print(addBinary(binStr1, binStr2))