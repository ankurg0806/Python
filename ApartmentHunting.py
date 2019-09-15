# "​↵Apartment Hunting↵​↵You're looking to move into a new apartment, and you're given a list of blocks where each block contains an apartment that you could move into. In order to pick your apartment, you want to optimize its location. You also have a list of requirements: a list of buildings that are important to you. For instance, you might value having a school and a gym near your apartment. The list of blocks that you have contains information at every block about all of the buildings that are present and absent at the block in question. For instance, for every block, you might know whether a school, a pool, an office, and a gym are present or not. In order to optimize your life, you want to minimize the farthest distance you'd have to walk from your apartment to reach all of your required buildings. Write a function that takes in a list of blocks and a list of your required buildings and that returns the location (the index) of the block that is most optimal for you.

# Sample input:
# [
	# {    "gym": False,
		 # "school": True,
		 # "store": False  
	# },  
	# {    "gym": True,
		 # "school": False,
		 # "store": False,
	# },
	# {    "gym": True,"
		 # "school": True,
		 # "store": False,
	# },
	# {    "gym": False,"
		 # "school": True,
		 # "store": False,
	# },
	# {    "gym": False,"
		 # "school": True,
		 # "store": True,
	# }
# ]

	# Req : ["gym", "school", "store"]
	# Output : 3 as from 3rd block, everything is at a distance of 1 thus minimum distance


def apartmentHunting(blocks, reqs):
    # Write your code here.
	maxDistanceForAnyReqForBlock = [float("-inf") for block in blocks]
	for i in range(len(blocks)):
		for req in reqs:
			closestDisForThisReq = float("inf")
			for j in range(len(blocks)):
				if blocks[j][req]:
					closestDisForThisReq = min(closestDisForThisReq, distance(i,j))
			maxDistanceForAnyReqForBlock[i] = max(maxDistanceForAnyReqForBlock[i],closestDisForThisReq)
	return idOfBlockWithMinVal(maxDistanceForAnyReqForBlock)

def idOfBlockWithMinVal(array):
	minVal = float("inf")
	for i in range(len(array)):
		if array[i] < minVal:
			minVal = array[i]
			index = i
	return index
			

def distance(i, j):
	return abs(i-j)
	
# Add, edit, or remove tests in this file.
# Treat it as your playground!

import program
import unittest


class TestProgram(unittest.TestCase):
    
    def test_case_1(self):
        blocks = [
            {
                "gym": False,
                "school": True,
                "store": False,
            },
            {
                "gym": True,
                "school": False,
                "store": False,
            },
            {
                "gym": True,
                "school": True,
                "store": False,
            },
            {
                "gym": False,
                "school": True,
                "store": False,
            },
            {
                "gym": False,
                "school": True,
                "store": True,
            },
        ]
        reqs = ["gym", "school", "store"]
        self.assertEqual(program.apartmentHunting(blocks, reqs), 3)
    
    def test_case_2(self):
        blocks = [
            {
                "gym": False,
                "office": True,
                "school": True,
                "store": False,
            },
            {
                "gym": True,
                "office": False,
                "school": False,
                "store": False,
            },
            {
                "gym": True,
                "office": False,
                "school": True,
                "store": False,
            },
            {
                "gym": False,
                "office": False,
                "school": True,
                "store": False,
            },
            {
                "gym": False,
                "office": False,
                "school": True,
                "store": True,
            },
        ]
        reqs = ["gym", "office", "school", "store"]
        self.assertEqual(program.apartmentHunting(blocks, reqs), 2)

    def test_case_3(self):
        blocks = [
            {
                "gym": False,
                "office": True,
                "school": True,
                "store": False,
            },
            {
                "gym": True,
                "office": False,
                "school": False,
                "store": False,
            },
            {
                "gym": True,
                "office": False,
                "school": True,
                "store": False,
            },
            {
                "gym": False,
                "office": False,
                "school": True,
                "store": False,
            },
            {
                "gym": False,
                "office": False,
                "school": True,
                "store": False,
            },
            {
                "gym": False,
                "office": False,
                "school": True,
                "store": True,
            },
        ]
        reqs = ["gym", "office", "school", "store"]
        self.assertEqual(program.apartmentHunting(blocks, reqs) in [2, 3], True)

    def test_case_4(self):
        blocks = [
            {
                "foo": True,
                "gym": False,
                "kappa": False,
                "office": True,
                "school": True,
                "store": False,
            },
            {
                "foo": True,
                "gym": True,
                "kappa": False,
                "office": False,
                "school": False,
                "store": False,
            },
            {
                "foo": True,
                "gym": True,
                "kappa": False,
                "office": False,
                "school": True,
                "store": False,
            },
            {
                "foo": True,
                "gym": False,
                "kappa": False,
                "office": False,
                "school": True,
                "store": False,
            },
            {
                "foo": True,
                "gym": True,
                "kappa": False,
                "office": False,
                "school": True,
                "store": False,
            },
            {
                "foo": True,
                "gym": False,
                "kappa": False,
                "office": False,
                "school": True,
                "store": True,
            },
        ]
        reqs = ["gym", "school", "store"]
        self.assertEqual(program.apartmentHunting(blocks, reqs) in [4, 5], True)

    def test_case_5(self):
        blocks = [
            {
                "gym": True,
                "school": True,
                "store": False,
            },
            {
                "gym": False,
                "school": False,
                "store": False,
            },
            {
                "gym": False,
                "school": True,
                "store": False,
            },
            {
                "gym": False,
                "school": False,
                "store": False,
            },
            {
                "gym": False,
                "school": False,
                "store": True,
            },
            {
                "gym": True,
                "school": False,
                "store": False,
            },
            {
                "gym": False,
                "school": False,
                "store": False,
            },
            {
                "gym": False,
                "school": False,
                "store": False,
            },
            {
                "gym": False,
                "school": False,
                "store": False,
            },
            {
                "gym": False,
                "school": True,
                "store": False,
            },
        ]
        reqs = ["gym", "school", "store"]
        self.assertEqual(program.apartmentHunting(blocks, reqs), 2)

    def test_case_6(self):
        blocks = [
            {
                "gym": True,
                "pool": False,
                "school": True,
                "store": False,
            },
            {
                "gym": False,
                "pool": False,
                "school": False,
                "store": False,
            },
            {
                "gym": False,
                "pool": False,
                "school": True,
                "store": False,
            },
            {
                "gym": False,
                "pool": False,
                "school": False,
                "store": False,
            },
            {
                "gym": False,
                "pool": False,
                "school": False,
                "store": True,
            },
            {
                "gym": True,
                "pool": False,
                "school": False,
                "store": False,
            },
            {
                "gym": False,
                "pool": False,
                "school": False,
                "store": False,
            },
            {
                "gym": False,
                "pool": False,
                "school": False,
                "store": False,
            },
            {
                "gym": False,
                "pool": False,
                "school": False,
                "store": False,
            },
            {
                "gym": False,
                "pool": False,
                "school": True,
                "store": False,
            },
            {
                "gym": False,
                "pool": True,
                "school": False,
                "store": False,
            },
        ]
        reqs = ["gym", "pool", "school", "store"]
        self.assertEqual(program.apartmentHunting(blocks, reqs), 7)

    def test_case_7(self):
        blocks = [
            {
                "gym": True,
                "office": False,
                "pool": False,
                "school": True,
                "store": False,
            },
            {
                "gym": False,
                "office": False,
                "pool": False,
                "school": False,
                "store": False,
            },
            {
                "gym": False,
                "office": True,
                "pool": False,
                "school": True,
                "store": False,
            },
            {
                "gym": False,
                "office": True,
                "pool": False,
                "school": False,
                "store": False,
            },
            {
                "gym": False,
                "office": False,
                "pool": False,
                "school": False,
                "store": True,
            },
            {
                "gym": True,
                "office": True,
                "pool": False,
                "school": False,
                "store": False,
            },
            {
                "gym": False,
                "office": False,
                "pool": True,
                "school": False,
                "store": False,
            },
            {
                "gym": False,
                "office": False,
                "pool": False,
                "school": False,
                "store": False,
            },
            {
                "gym": False,
                "office": False,
                "pool": False,
                "school": False,
                "store": False,
            },
            {
                "gym": False,
                "office": False,
                "pool": False,
                "school": True,
                "store": False,
            },
            {
                "gym": False,
                "office": False,
                "pool": True,
                "school": False,
                "store": False,
            },
        ]
        reqs = ["gym", "pool", "school", "store"]
        self.assertEqual(program.apartmentHunting(blocks, reqs), 4)
	

if __name__ == "__main__":
	unittest.main()


	
# Solution Time Complexity : O(B*B*r)

# Can we solve it in O(B*r)
# Really complex code, The sole purpose is to build a table like below,

	# Block    0   1   2   3   4
	# Gym      1   0   0   1   2
	# School   0   1   0   0   0 
	# Store    4   3   2   1   0
	
	# And If we see each column, the minimum is for block 3. If we can build this table in O(b*r) time, this problem can be solved in that time
	
	# Below code has used lambdas with map(), minDistanceFromBlocks is calculating the three lists (1 per request). maxDistanceForBlocks is calculating the max for each block
	
def apartmentHunting(blocks, reqs):
    # Write your code here.
	minDistanceFromBlocks = list(map(lambda req: getMinDistances(req, blocks), reqs))
	maxDistanceForBlocks = getMaxDistanceForBlocks(blocks, minDistanceFromBlocks)
	return idOfBlockWithMinVal(maxDistanceForBlocks)
	
def getMinDistances(req, blocks):
	minDis = [0 for b in blocks]
	closestReqId = float("inf")
	for i in range(len(blocks)):
		if blocks[i][req]:
			closestReqId = i
		minDis[i] = distance(i,closestReqId)
	for i in reversed(range(len(blocks))):
		if blocks[i][req]:
			closestReqId = i
		minDis[i] = min (minDis[i], distance(i, closestReqId))
	return minDis
	
def getMaxDistanceForBlocks(blocks, minDistanceFromBlocks):
	maxDisAtBlocks = [0 for b in blocks]
	for i in range(len(blocks)):
		minDisAtBlock = list(map(lambda distances: distances[i], minDistanceFromBlocks))
		maxDisAtBlocks[i] = max(minDisAtBlock)
	return maxDisAtBlocks
		
def idOfBlockWithMinVal(array):
	minVal = float("inf")
	for i in range(len(array)):
		if array[i] < minVal:
			minVal = array[i]
			index = i
	return index
			

def distance(i, j):
	return abs(i-j)