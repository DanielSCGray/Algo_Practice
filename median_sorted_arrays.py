# Median of Sorted Arrays
# Given two arrays that are sorted but not necessarily the same length, find the median value. For
# example, if given ([1,5,9], [1,2,3,4,5,6])​, return 4​. If the number of values is even, return the
# average of the two middle values. if given ([1,5,9], [1,2,3,4,5])​, return 3.5​.

    #I see this as two parts: a merge function and a median finder. I will build both then use them for the three parts of the question
def merge(nums1, nums2):
    total_len = len(nums1) + len(nums2)
    combined_array = []
    for i in range(total_len):
        if not len(nums1) > 0:
            combined_array.extend(nums2)
            break
        elif not len(nums2) > 0:
            combined_array.extend(nums1)
            break
        if nums1[0] > nums2[0]:
            val = nums2.pop(0)
            combined_array.append(val)
        else:
            val = nums1.pop(0)
            combined_array.append(val)
    return combined_array

test = merge([1,5,9], [1,2,3,4,5,6])
print(test)
#[1, 1, 2, 3, 4, 5, 5, 6, 9]

def median_finder(arr):
    length = len(arr)
    mid = length // 2
    if length % 2 != 0:
        return arr[mid]
    else:
        return ((arr[mid]+ arr[mid - 1])/ 2)


print(median_finder(test))
#4

#First:

def median_of_sorted_arrays1(arr1, arr2):
    combined = merge(arr1, arr2)
    return median_finder(combined)

print(median_of_sorted_arrays1([1,5,9], [1,2,3,4,5,6]))
#4

# Second:​ Expand your function to accept three arrays instead of two.
def median_of_sorted_arrays2(arr1, arr2, arr3):
    first_merge = merge(arr1, arr2)
    combined = merge(first_merge, arr3)

    return median_finder(combined)

print(median_of_sorted_arrays2([1,5,9], [1,2,3,4,5,6], [1,2,10,13,15]))
#4.5

# Third:​ Rework your function to correctly handle an arbitrary number of arrays.

def median_of_sorted_arrays3(arr1, arr2, *args):
    combined = merge(arr1, arr2)
    for arr in args:
        temp_list = merge(combined, arr)
        combined = temp_list
    return median_finder(combined)

print(median_of_sorted_arrays3([1,5,9], [1,2,3,4,5,6], [1,2,10,13,15]))
#4.5
print(median_of_sorted_arrays3([1,5,9], [1,2,3,4,5,6], [1,2,10,13,15], [2,4,7], [1,3,4,6,99]))
#4.0