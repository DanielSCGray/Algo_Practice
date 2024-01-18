# rBinarySearch
# Write a recursive function that, given a sorted
# array and a value, determines whether the value
# is found within the array. For example,
# rBinarySearch([1,3,5,6], 4) = false;
# rBinarySearch([4,5,6,8,12], 5) = true.

def bin_search(arr: list, num):
    if len(arr) == 0:
        return False
    val = arr.pop()
    if val == num:
        return True
    elif val < num:
        #this works because the list is sorted -> every val that follows will be less than num as well
        return False
    else:
        return bin_search(arr, num)
    
print(bin_search([1,3,5,6], 4))
#false
print(bin_search([4,5,6,8,12], 5))
#true
