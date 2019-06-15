'''

Write a function that takes an array as input and return an array of size 2, which has the largest name
of numbers contained in that array.

The first number in the output should be the first number in the range and the second number in the output
should be the last number in the range. Note that Range is a set of consecutive numbers that comes one after
another in the real numbers

e.g.
Sample input
[1,11,3,0,15,5,2,4,10,7,12,6]
Output [0,7]
because the array contains 0 to 7 all real numbers

One approach could be to sort them and then in single iteration, find the longest range which 
have consecutive numbers. This approach will take O(nlogn) time based on the sorting algorithm

Following is the solution in which we use hashing and we utilize O(n) space complexity but the solution 
take O(n) time to find the longest range
'''

def largestRange(array):
    outputRange = []
    maxLength = 0
    # nums is the hashtable that stores key values where key : numbers in array and value: true/False
    # based on whether I need to traverse this key in array or not.
    nums = {}
    # initially all keys should have value true because I need to traverse each of them
    for num in array:
        nums[num] = True
    for num in array:
        if not nums[num]:
            continue
        nums[num] = False
        count = 1
        left = num - 1
        right = num + 1
        while left in nums:
            count += 1
            left -=1
        while right in nums:
            count += 1
            right += 1
        if count > maxLength:
            maxLength = count
            outputRange = [left + 1, right - 1]
    return outputRange
    
myarray = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]
outputArray = largestRange(myarray)
print(("Range : [{} , {}]").format(outputArray[0], outputArray[1]))
