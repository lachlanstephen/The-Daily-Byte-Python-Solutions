# Given an array of strings, return the longest common prefix that is shared amongst all strings.
# Note: you may assume all strings only contain lowercase alphabetical characters.

# Ex: Given the following arrays...

# ["colorado", "color", "cold"], return "col"
# ["a", "b", "c"], return ""
# ["spot", "spotty", "spotted"], return "spot"

wordArr = ["testament", "tester", "testicle"]

def longestCommonPrefix(arr):
    result = arr[0]
    for str in arr[1:]:
        for i in range(len(result)):
            if i == len(str) or str[i] != result[i]:
                result = result[0:i]
                break
    return result

print(longestCommonPrefix(wordArr))
