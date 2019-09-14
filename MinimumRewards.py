# Minimum Rewards Problem

# Imagine that you're a teacher who's just graded the final exam in a class. You have a list of student scores on the final exam in a particular order (not necessarily sorted), and you want to reward your students. You decide to do so fairly by giving them arbitrary rewards following two rules: first, all students must receive at least one reward; second, any given student must receive strictly more rewards than an adjacent student (a student immediately to the left or to the right) with a lower score and must receive strictly fewer rewards than an adjacent student with a higher score. Assume that all students have different scores; in other words, the scores are all unique. Write a function that takes in a list of scores and returns the minimum number of rewards that you must give out to students, all the while satisfying the two rules.

# Sample input: [8, 4, 2, 1, 3, 6, 7, 9, 5]
# Sample output: 25 ([4, 3, 2, 1, 2, 3, 4, 5, 1])

def minRewards(scores):
    # Write your code here.
	rewards = [1 for _ in scores]
	for i in range(1, len(scores)):
		if scores[i] > scores[i-1]:
			rewards [i] = rewards[i-1] + 1
	for i in range(len(scores) - 1, 0, -1):
		if scores[i-1] > scores [i]:
			rewards[i-1] = max(rewards[i-1], rewards[i]+1)
	print (rewards)
	return sum(rewards)
	
# Add, edit, or remove tests in this file.
# Treat it as your playground!

import program
import unittest


class TestProgram(unittest.TestCase):
	
	def test_case_1(self):
		self.assertEqual(program.minRewards([1]), 1)
	
	def test_case_2(self):
		self.assertEqual(program.minRewards([5, 10]), 3)
	
	def test_case_3(self):
		self.assertEqual(program.minRewards([10, 5]), 3)

	def test_case_4(self):
		self.assertEqual(program.minRewards([4, 2, 1, 3]), 8)
	
	def test_case_5(self):
		self.assertEqual(program.minRewards([0, 4, 2, 1, 3]), 9)
	
	def test_case_6(self):
		self.assertEqual(program.minRewards([8, 4, 2, 1, 3, 6, 7, 9, 5]), 25)
	
	def test_case_7(self):
		self.assertEqual(program.minRewards([2, 20, 13, 12, 11, 8, 4, 3, 1, 5, 6, 7, 9, 0]), 52)
	
	def test_case_8(self):
		self.assertEqual(program.minRewards([2, 1, 4, 3, 6, 5, 8, 7, 10, 9]), 15)
	
	def test_case_9(self):
		self.assertEqual(program.minRewards([800, 400, 20, 10, 30, 60, 70, 90, 17, 21, 22, 13, 12, 11, 8, 4, 2, 1, 3, 6, 7, 9, 0, 68, 55, 67, 57, 60, 51, 661, 50, 65, 53]), 93)
	

if __name__ == "__main__":
	unittest.main()
