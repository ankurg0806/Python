# Find Set of numbers from a sorted array that adds up to a given number

# Recursive Solution
def count_set(numList, givenSum):
    return recursive_count(numList, givenSum, len(numList) - 1)

def recursive_count(numList, givenSum, k):
    if givenSum == 0:
        return 1 
    elif givenSum < 0:
        return 0
    elif k < 0:
        return 0
    elif numList[k] > givenSum:
        return recursive_count(numList, givenSum, k -1)
    else:
        return recursive_count(numList, givenSum - numList[k], k-1) + recursive_count(numList, givenSum, k-1)

mylist = [2, 4, 6, 10]
print(count_set(mylist, 16))

# Dynamic Programming Solution
def count_set_dp(numList, givenSum):
    mydict = {}
    return recursive_count_dp(numList, givenSum, len(numList) - 1, mydict)

def recursive_count_dp(numList, givenSum, k, mydict):
    key = str(givenSum) + ':' + str(k)
    if key in mydict:
        return mydict[key]
    elif givenSum == 0:
        return 1 
    elif givenSum < 0:
        return 0
    elif k < 0:
        return 0
    elif numList[k] > givenSum:
        to_return = recursive_count_dp(numList, givenSum, k -1)
    else:
        to_return = recursive_count_dp(numList, givenSum - numList[k], k-1, mydict) + recursive_count_dp(numList, givenSum, k-1, mydict)
    mydict[key] = to_return
    print(mydict)
    return to_return
	
mylist = [2, 4, 6, 10]
print(count_set_dp(mylist, 16))

# TimeComplexity <= 2*n*givenSum thus O(T*N) as we are looping on givenSum (till it reduce to 0) and array (from len to 0)

        

