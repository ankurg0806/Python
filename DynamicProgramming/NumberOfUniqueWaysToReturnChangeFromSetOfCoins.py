# No of unique ways to make change from a set of available coins

def numberOfWaysToMakeChange(n, denoms):
	ways = [0 for amount in range(n + 1)]
	ways[0] = 1
	for coin in denoms:
		for amount in range(1, n + 1):
			if amount >= coin:
				ways[amount] += ways[amount- coin]
	return ways[n]
	
print(numberOfWaysToMakeChange(12, [1,2,5])