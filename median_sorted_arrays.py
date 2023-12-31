# Median of Sorted Arrays
# Given two arrays that are sorted but not necessarily the same length, find the median value. For
# example, if given ([1,5,9], [1,2,3,4,5,6])​, return 4​. If the number of values is even, return the
# average of the two middle values. if given ([1,5,9], [1,2,3,4,5])​, return 3.5​.

#will make a merge helper function
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

print(merge([1,5,9], [1,2,3,4,5,6]))


def median_finder(nums1, nums2):
    pass





# Second:​ Expand your function to accept three arrays instead of two.
# Third:​ Rework your function to correctly handle an arbitrary number of arrays.
