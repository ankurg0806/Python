# Write a function that takes in two non-empty arrays of integers. The function should find the pair of numbers (one from the first array, one from the second array) whose absolute difference is closest to zero. The function should return an array containing these two numbers, with the number from the first array in the first position. Assume that there will only be one pair of numbers with the smallest difference.

# Instead of generating all possible pairs of numbers, try somehow only looking at pairs that you know could actually have the smallest difference. How can you accomplish this?
# Would it help if the two arrays were sorted? If the arrays were sorted and you were looking at a given pair of numbers, could you efficiently find the next pair of numbers to look at? What are the runtime implications of sorting the arrays?
# Start by sorting both arrays, as per Hint #2. Put a pointer at the beginning of both arrays and evaluate the absolute difference of the pointer-numbers. If the difference is equal to zero, then you've found the closest pair; otherwise, increment the pointer of the smaller of the two numbers to find a potentially better pair. Continue until you get a pair with a difference of zero or until one of the pointers gets out of range of its array.

# Sample input: [-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]

def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
	arrayOne.sort()
	arrayTwo.sort()
	smallest = float("inf")
	i = 0
	j = 0
	smallestpair = []
	while i < len(arrayOne) and j < len(arrayTwo):
		if arrayOne[i] < arrayTwo[j]:
			current = arrayTwo[j] - arrayOne[i]
			if (current < smallest):
			    smallest = current
			    smallestPair = [arrayOne[i],arrayTwo[j]]
			i += 1
		elif arrayOne[i] > arrayTwo[j]:
			current = arrayOne[i] - arrayTwo[j]
			if (current < smallest):
			    smallest = current
			    smallestPair = [arrayOne[i],arrayTwo[j]]
			j += 1
		else:
			return [arrayOne[i],arrayTwo[j]]
	return smallestPair