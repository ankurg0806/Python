# Write a function that returns the common elements (as an array) between two sorted arrays of integers (ascending order). 

# Example: The common elements between [1, 3, 4, 6, 7, 9] and [1, 2, 4, 5, 9, 10] are [1, 4, 9]. 


def count_common(arr1, arr2):
    result = []
    index1 = 0 
    index2 = 0
    while index1 < len(arr1) and index2 < len(arr2):
        if arr1[index1] == arr2[index2]:
            result.append(arr1[index1])
            index1 += 1
            index2 += 1 
        else:
            val = min(arr1[index1], arr2[index2])
            if arr1[index1] == val:
                index1 += 1
            else:
                index2 += 1 
    return result

list_a1 = [1, 2, 9, 10, 11, 12]
list_a2 = [0, 1, 2, 3, 4, 5, 8, 9, 10, 12, 14, 15]
print(count_common(list_a1, list_a2))

# Time Complexity
# O(max(n + m)) time complexity, where n is the number of elements in array 1, and m is the number of elements in array 2.
    