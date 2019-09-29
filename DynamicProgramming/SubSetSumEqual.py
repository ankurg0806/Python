# Can you partition your array in to two subsets in such a way that sum of the two subsets are equal
# This is a variation of 0-1 Knapsack problem

def subsetSum(A):
    totalSum = 0;
    for num in A:
        totalSum += num
        
    if totalSum % 2 == 1:
        return False
    
    mat = [[False for i in range(totalSum//2+1)]for j in range(len(A)+1)]
    mat[0][0] = True
    for j in range(1,totalSum//2+1):
        mat[0][j] = False
    for j in range(1,len(A)+1):
        mat[j][0] = True
    for i in range(1, len(mat)):
        for j in range(1, len(mat[0])):
            print(mat[i][j])
            prevRowisTrue = mat[i-1][j] 
            isExactMatch = A[i-1] == j
            canArriveAtSum = False
            if j > A[i-1]:
                remainingSum = j - A[i-1]
                canArriveAtSum = mat[i-1][remainingSum]
            mat[i][j] = prevRowisTrue or isExactMatch or canArriveAtSum
    print(mat)
    return mat[len(A)][totalSum//2]

print (subsetSum([3,5,12,4,5,7]))

# The matrix will look like this
      # 0     1     2      3  	4		5		6		7	8		9		10	  11	 12 	13     14     15     16    17     18
# 0 [[True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], 
# 3  [True, False, False, True,  False, False, False, False, False, False, False, False, False, False, False, False, False, False, False], 
# 5  [True, False, False, True,  False, True,  False, False, True,  False, False, False, False, False, False, False, False, False, False], 
# 12 [True, False, False, True,  False, True,  False, False, True,  False, False, False, True,  False, False, True,  False, True,  False], 
# 4  [True, False, False, True,  True,  True,  False, True,  True,  True,  False, False, True,  False, False, True,  True,  True,  False], 
# 5  [True, False, False, True,  True,  True,  False, True,  True,  True,  True,  False, True,  True,  True,  True,  True,  True,  False], 
# 7  [True, False, False, True,  True,  True,  False, True,  True,  True,  True,  True,  True,  True,  True,  True,  True,  True,  False]]

# Time Complexity : O (n* sumOfNums/2)

# Can I reduce the space complexity
