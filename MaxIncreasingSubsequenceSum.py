# Max Sum Increasing Subsequence

# Given an non-empty array of integers, write a function that returns an array of length 2. The first element in the output array should be an integer value representing the greatest sum that can be generated from a strictly-increasing subsequence in the array. The second element should be an array of the numbers in that subsequence. A subsequence is defined as a set of numbers that are not necessarily adjacent but that are in the same order as they appear in the array. Assume that there will only be one increasing subsequence with the greatest sum.

# Sample input: [10, 70, 20, 30, 50, 11, 30]
# Sample output: [110, [10, 20, 30, 50]]

def maxSumIncreasingSubsequence(array):
    # Write your code here.
  sums = array[:]
  maxi = 0
  sequences = [None for x in array]
  for i in range(len(array)):
    current = array[i]
    for j in range(0,i):
      if current> array[j] and sums[j] + current > sums[i]:
        sums[i] = sums[j] + current
        sequences[i] = j
    if sums[i] >= sums[maxi]:
      maxi = i
  return [sums[maxi],buildSeq(array,sequences,maxi)]

def buildSeq(array,sequences, maxi):
  sequence = []
  while maxi is not None:
    sequence.append(array[maxi])
    maxi = sequences[maxi]
  return list(reversed(sequence))
