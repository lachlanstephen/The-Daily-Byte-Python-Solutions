# Given an array of integers, return whether or not two numbers sum to a given target, k.
# Note: you may not sum a number with itself.

# Ex: Given the following...

# [1, 3, 8, 2], k = 10, return true (8 + 2)
# [3, 9, 13, 7], k = 8, return false
# [4, 2, 6, 5, 2], k = 4, return true (2 + 2)

intArray = [3, 9, 13, 7, 4, 3, 8, 13, 2, 7, 9, 6]
k = 19


# My Solution
# Time Complexity - O(N²)

def twoSum(arr, tar):
    for i in range(len(arr)):
        for j in arr[i + 1:]:
            if arr[i] + j == tar:
                return True
    return False

print(twoSum(intArray, k))


# Daily Byte Guided Solution

def twoSumHash(arr, tar):
    vals = {}
    for i in range(len(arr)):
        if vals.get(tar - arr[i]):
            return True
        else:
            vals[arr[i]] = i
    return False
        
print(twoSumHash(intArray, k))