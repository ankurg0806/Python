# # Longest Common Subsequence

# Implement a function that returns the longest subsequence common to two given strings. A subsequence is defined as a group of characters that appear sequentially, with no importance given to their actual position in a string. In other words, characters do not need to appear consecutively in order to form a subsequence. Assume that there will only be one longest common subsequence.
# Sample input: "ZXVVYZW", "XKYKZPW"

# Sample output: ["X", "Y", "Z", "W"]

# Using tabulation method the table will look like this
     # 0    1   2    3     4     5      6      7
		  # X   K    Y     K     Z      P		 W
# 0  [['', '',  '',  '',   '',   '',    '',    ''],
# 1 Z ['', '',  '',  '',   '',   'Z',   'Z',   'Z'],
# 2 X ['', 'X', 'X', 'X',  'X',  'X',   'X',   'X'], 
# 3 V ['', 'X', 'X', 'X',  'X',  'X',   'X',   'X'], 
# 4 V ['', 'X', 'X', 'X',  'X',  'X',   'X',   'X'], 
# 5 Y ['', 'X', 'X', 'XY', 'XY', 'XY',  'XY',  'XY'], 
# 6 Z ['', 'X', 'X', 'XY', 'XY', 'XYZ', 'XYZ', 'XYZ'], 
# 7 W ['', 'X', 'X', 'XY', 'XY', 'XYZ', 'XYZ', 'XYZW']]

# this is a typical dynamic programming problem that can be solved with top down (recursive) approach and bottom up(tabulation approach)

def longestCommonSubsequence(str1, str2):
	mat = [['' for x in range(len(str2)+1)] for y in range(len(str1)+1)]
	for x in range(0,len(str1)):
		for y in range(0,len(str2)):
			if str1[x] == str2[y]:
				mat[x+1][y+1] = mat[x][y] + str1[x]
			else:
				mat[x+1][y+1] = max(mat[x+1][y],mat[x][y+1], key = len)
	return [x for x in mat[len(str1)][len(str2)]]

print(longestCommonSubsequence("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "CCCDDEGDHAGKGLWAJWKJAWGKGWJAKLGGWAFWLFFWAGJWKAGTUV"))

Time Complexity = Space Complexity = O(m*n)
