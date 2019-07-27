# Maximum Subset Sum With No Adjacent Elements

# Write a function that takes in an array of positive integers and returns an integer representing the maximum sum of non-adjacent elements in the array. If a sum cannot be generated, the function should return 0.

# Sample input: [75, 105, 120, 75, 90, 135]
# dp[0] = array[0]
	# dp[1] = max(array[0],array[1])
	# for i in range(2, len(array)):
		# dp[i] =  max(array[i] + dp[i-2], dp[i-1])
	# return dp[len(array)-1]
# Sample output: 330 (75, 120, 135)

# Hint1: 
# Try building an array of the same length as the input array. At each index in this new array, store the maximum sum that can be generated using no adjacent numbers located between index 0 and the current index.

# Hint2: 
# Can you come up with a formula that relates the max sum at index i to the max sums 

# Hint3:
# Do you really need to store the entire array mentioned in Hint #1, or can you somehow store just the max sums that you need at any point in time?

# Optimal time and space complexity
# O(n) time O(1) space

# This problem is a classical example of dynamic programming

# Let's suppose DP[i] is the maximum value so far when you are at index i in the array such that no to adjacent numbers are there till index i. You can represent DP[i] as,

# DP[i] = max(value[i] + DP[i-2], DP[i-1])

# Here, value[i] + DP[i-2] is the case when you decide that you are picking the current value at index i, and as per the problem, since you can't select the value at index i-1 in this case, thus you should add this value[i] with the max sum you have obtained till pos i-2, i.e. DP[i-2]

# Second case is DP[i-1], that means you are not selecting the value at index[i] thus you can select the max sum obtained till pos i-1 i.e. DP[i-1] and then you can select the max of two which represents the formula at any position i.

def maxSubsetSumNoAdjacent(array):
  dp = []
  if len(array) == 0:
    return 0
  elif len(array) is 1:
    return array[i]
  elif len(array) is 2:
	  return max(array[0], array[1])
  dp.insert(0, array[0])
  dp.insert(1, max(array[0],array[1]))
  for i in range(2,len(array)):
    dp.insert(i, max(array[i] + dp[i-2], dp[i-1]))
  return dp[i]
print(maxSubsetSumNoAdjacent([75, 105, 120, 75, 90, 135]))

# For this approach the time complexity is O(n) but space complexity is O(n) as well
# We could further reduce the space complexity we storing intermediate results in two variables because Once I calculate max sum at current position and current -1 position, I don't need the sums prior to those.

def maxSubsetSumNoAdjacent(array):
  if len(array) == 0:
    return 0
  elif len(array) is 1:
    return array[i]
  elif len(array) is 2:
	  return max(array[0], array[1])
  a = array[0]
  b = max(array[0],array[1])
  for i in range(2,len(array)):
    maximum = max(array[i] + a, b)
    a = b
    b = maximum
  return maximum
print(maxSubsetSumNoAdjacent([75, 105, 120, 75, 90, 135]))