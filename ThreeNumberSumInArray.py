def threeNumberSum(array, targetSum):
    # Write your code here.
	array.sort()
	triplets = []
	for i in range(len(array) - 2):
		left = i + 1
		right = len(array) - 1
		while left < right:
			curr_sum = array[i] + array[left] + array[right]
			if curr_sum == targetSum:
				triplets.append([array[i], array[left], array[right]])
				left += 1
				right -= 1
			elif curr_sum > targetSum:
				right -= 1
			elif curr_sum < targetSum:
				left += 1
	return triplets
