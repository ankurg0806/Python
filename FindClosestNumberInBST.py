# Find Closest Value In BST
# You are given a BST data structure consisting of BST nodes. Each BST node has an integer value stored in a property called "value" and two children nodes stored in properties called "left" and "right," respectively. A node is said to be a BST node if and only if it satisfies the BST property: its value is strictly greater than the values of every node to its left; its value is less than or equal to the values of every node to its right; and both of its children nodes are either BST nodes themselves or None (null) values. 
# You are also given a target integer value; write a function that finds the closest value to that target value contained in the BST. 
# Assume that there will only be one closest value.
# Sample input:            10          , 12
						# /  \
					   # 5    15
					  # / \  /  \
					 # 2   5 13  22
					# /        \
				   # 1          14
# Sample output: 13

# Try traversing the BST node by node, all the while keeping track of the node with the value closest to the target value. 
# Calculating the absolute value of the difference between a node's value and the target value should allow you to check if that node is closer than the current closest one

# Iterative Solution
def findClosestValueInBst(tree, target):
    # Write your code here.
	closest  = float('inf')
	number = 0
	currentNode = tree
	while currentNode is not None:
		if abs(target - currentNode.value) < closest:
			closest = abs(target - currentNode.value)
			number = currentNode.value
		if target > currentNode.value:
			currentNode = currentNode.right
		else:
			currentNode = currentNode.left
	return number
		
# Recursive Solution
closest = float("inf")
number = 0
def findClosestValueInBst(tree, target):
  global closest
  global number
  if tree == None:
    closest = float("inf")
    return number
  if abs(target - tree.value) < closest:
    closest = abs(target - tree.value)
    number = tree.value
    print (closest)
  if (target > tree.value):
    findClosestValueInBst(tree.right, target)
  elif (target < tree.value):
    findClosestValueInBst(tree.left, target)
  else:
    closest = float("inf")
    return number
  return number
  
# Code to test Solution
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
        return self

test = BST(100).insert(5).insert(15).insert(5).insert(2).insert(1).insert(22) \
.insert(1).insert(1).insert(3).insert(1).insert(1).insert(502).insert(55000) \
.insert(204).insert(205).insert(207).insert(206).insert(208).insert(203) \
.insert(-51).insert(-403).insert(1001).insert(57).insert(60).insert(4500)


class TestProgram(unittest.TestCase):

	def test_case_1(self):
		self.assertEqual(findClosestValueInBst(test, 100), 100)

	def test_case_2(self):
		self.assertEqual(findClosestValueInBst(test, -70), -51)


if __name__ == "__main__":
	unittest.main()