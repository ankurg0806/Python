# Min Number Of Coins For Change

# Given an array of positive integers representing coin denominations and a single non-negative integer representing a target amount of money, implement a function that returns the smallest number of coins needed to make change for that target amount using the given coin denominations. Note that an unlimited amount of coins is at your disposal. If it is impossible to make change for the target amount, return -1.

# Sample input: 7, [1, 5, 10]
# Sample output: 3 (2x1 + 1x5)

def minNumberOfCoinsForChange(n, denoms):
    # Write your code here.
	ways = [0 for amount in range(n + 1)]
	ways[0] = 0
	for coin in denoms:
		for amount in range(1, n + 1):
		  if amount == coin:
			  ways[amount] = 1
		  elif amount > coin:
			  if ways[amount-coin] == 0:
				  ways[amount] = 0
			  else:
				  ways[amount] = ways[amount-coin] + 1
	print(ways)
	return ways[n] if ways[n]>0 else -1

print(minNumberOfCoinsForChange(7,[1,5,10]))