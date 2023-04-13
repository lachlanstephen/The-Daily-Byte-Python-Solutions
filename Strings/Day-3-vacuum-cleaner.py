# Given a string representing the sequence of moves a robot vacuum makes, return whether or not it will return to its original position. The string will only contain L, R, U, and D characters, representing left, right, up, and down respectively.

# Ex: Given the following strings...

# "LR", return true
# "URURD", return false
# "RUULLDRD", return true

inputString = "RUULLDRD"

def backToBase(str):
    route = str.lower()
    vacuum = {"u": 0, "d": 0, "l": 0, "r": 0}
    for char in route:
        vacuum[char] += 1
    return vacuum["u"] == vacuum["d"] and vacuum["l"] == vacuum["r"]

print(backToBase(inputString))