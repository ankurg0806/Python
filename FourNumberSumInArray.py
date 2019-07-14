
Four Number Sum
Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. The function should find all quadruplets in the array that sum up to the target sum and return a two-dimensional array of all these quadruplets in no particular order. If no four numbers sum up to the target sum, the function should return an empty array.

Sample input: [7, 6, 4, -1, 1, 2], 16

Sample output: [[7, 6, 4, -1], [7, 6, 1, 2]]

def fourNumberSum(array, targetSum):
    # Write your code here.
	allPairSum = {}
	quadruplets = []
	for i in range(1, len(array)-1):
		for j in range(i+1, len(array)):
			currSum = array[i] + array[j]
			diff = targetSum - currSum
			if diff in allPairSum:
				for pair in allPairSum[diff]:
					quadruplets.append(pair + [array[i],array[j]])
		for k in range(0, i):
			currSum = array[i] + array[k]
			if currSum not in allPairSum:
				allPairSum[currSum] = [[array[k], array[i]]]
			else:
				allPairSum[currSum].append([array[k], array[i]])
	return quadruplets
			