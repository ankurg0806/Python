Count distinct elements in every window of size k
Given an array of size n and an integer k, return the of count of distinct numbers in all windows of size k.
Example:

Input: arr[] = {1, 2, 1, 3, 4, 2, 3};
k = 4
Output:
3
4
4
3

Explanation:
First window is {1, 2, 1, 3}, count of distinct numbers is 3
Second window is {2, 1, 3, 4} count of distinct numbers is 4
Third window is {1, 3, 4, 2} count of distinct numbers is 4
Fourth window is {3, 4, 2, 3} count of distinct numbers is 3

This can be solved in linear time complexity using Sliding window technique. The idea is to keep track of distinct count of elements in current window of size k and keep sliding the window by 1 until you reach the end of the given array.

def myfunct(a, k):
    mylist = []
    mymap = {}
    dis_count = 0
    for i in range(0, k):
        if a[i] in mymap:
            mymap[a[i]] +=1
        else:
            dis_count += 1
            mymap[a[i]] = 1
    print(mymap)
    mylist.append(dis_count)
    for i in range(k, len(a)):
        # reduce the count of element at index that is now excluded from sliding window
        mymap[a[i-k]] -= 1
        # if this count has become 0, that means now we have one less distinct element to start with
        if mymap[a[i-k]] == 0:
            del mymap[a[i-k]]
            dis_count -= 1
        # check whether the newly included element at index i is already in map or not and modify the count accordingly
        if a[i] in mymap:
            mymap[a[i]] += 1
        else:
            dis_count += 1
            mymap[a[i]] = 1
        mylist.append(dis_count)
        print (mymap)
    return mylist
    
mylistOfDistinctElementCountsInEachSubArray = myfunct([10,15,6,71,18,47,33,23,28,29,30,6,66,32,45,73,70,90], 4)
print(mylistOfDistinctElementCountsInEachSubArray)

