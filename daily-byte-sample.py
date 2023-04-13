# Best Time to Buy and Sell Stock
# Given an array of integers where the ith integer represents the price of the stock on day i, return the largest possible profit from completing one transaction (i.e. buying 1 share and selling 1 share).
# Examples: Given the following prices...

# // Buy on day 1 and sell on day 5 for a profit of 5 - 1 = 4. 
# prices = [1, 2, 3, 4, 5], return 4. 
# // Buy on day 4 and sell on day 9 for a profit of 11 - 1 = 10. 
# prices = [4, 5, 2, 1, 6, 10, 4, 9, 11], return 10. 
# // Buying and selling the stock at any point would yield a negative profit. 
# prices = [33, 18, 8, 2], return 0 


#TO USE A RANDOM PRICE INPUI

# import random

# prices = [random.randint(0, 1000000000) for _ in range(10000000)]

prices = [4, 5, 2, 1, 6, 10, 4, 9, 11]


# My Solution

def myMoneyMaking(arr):
    n = len(arr)
    currentLow = arr[0]
    lowIdx = 0
    profit = 0
    for i in range(n):
        if arr[i] < currentLow:
            currentLow = arr[i]
            lowIdx = i
    for j in range(lowIdx, n):
        if arr[j] - arr[lowIdx] > profit:
            profit = arr[j] - arr[lowIdx]
    return profit

#print(myMoneyMaking(prices))


#Baily Byte Solution

def dbMoneyMaking(arr):
    profit = 0
    low = arr[0]
    for i in range(len(arr)):
        if arr[i] > low:
            profit = max(profit, arr[i] - low)
        else:
            low = arr[i]
    return profit

print(dbMoneyMaking(prices))



