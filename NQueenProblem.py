# N Queen Problem : Backtracking

# Solution

print ("Enter the number of queens")
N = int(input())

#chessboard
#NxN matrix with all elements 0
board = [[0]*N for _ in range(N)]

def can_place(row, col):
    #since we are filling one column at a time,
	# we will check if no queen is placed in that particular row (the row for which we called can_place method)
    for k in range(0, col):
        if board[row][k]==1:
            return False
    #Upper Diagonal
    r,c = row, col
    while r >=0 and c >=0:
      if board[r][c] == 1:
        return False
      r -=1
      c -=1
    
    #Lower Diagonal
    r,c = row, col
    while r < len(board) and c >=0:
      if board[r][c] == 1:
        return False
      r +=1
      c -=1
    return True 

def N_queen(q, n):
    #if n is 0, solution found
    if q==n:
        return True
    for i in range(0,n):
      if can_place(i, q):
        board[i][q] = 1
        #recursion
        #wether we can put the next queen with this arrangment or not
        if N_queen(q+1, n)==True:
            return True
        board[i][q] = 0
    return False

if N_queen(0,N) is True:
    for i in board:
        print (i)
else:
    print("NO")
	
# Output:
# Enter the number of queens
# 5
# [1, 0, 0, 0, 0]
# [0, 0, 0, 1, 0]
# [0, 1, 0, 0, 0]
# [0, 0, 0, 0, 1]
# [0, 0, 1, 0, 0]
