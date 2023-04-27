# Given an array of integers, return whether or not two numbers sum to a given target, k.
# Note: you may not sum a number with itself.

# Ex: Given the following...

# [1, 3, 8, 2], k = 10, return true (8 + 2)
# [3, 9, 13, 7], k = 8, return false
# [4, 2, 6, 5, 2], k = 4, return true (2 + 2)

intArray = [3, 9, 13, 7, 4, 3, 8, 13, 2, 7, 9, 6]
k = 19

def twoSum(arr, tar):
    for i in range(len(arr)):
        for j in arr[i + 1:]:
            if arr[i] + j == tar:
                print(str(arr[i]) + " + " + str(j))
                return True
    return False

print(twoSum(intArray, k))