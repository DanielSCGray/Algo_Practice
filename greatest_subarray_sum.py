# Max of Subarray Sums
# Given a numerical array that is potentially very long, return the maximum sum of values from a
# subarray. Any consecutive sequence of indices in the array is considered a subarray. Create a function
# that returns the highest sum possible from these subarrays. Given [1,2,-4,3,-2,3,-1]​, you should
# return 4​ (for subarray [3,-2,3]​), and given [-1,-2,-4,-3,-2,-3]​, return 0​ (for []​). This problem
# has many possible implementations. Which do you prefer & why?

def max_sub_sum(array):
    i = 0 
    greatest_sum = 0
    current_sum =0 
    while i < len(array)-1:
        if array[i] < 0:
            current_sum = 0 
            i+=1 
            continue
        current_sum = array[i]
        if current_sum > greatest_sum:
            greatest_sum = current_sum
        j = i + 1 
        while j < len(array):
            current_sum += array[j]
            if current_sum > greatest_sum:
                greatest_sum = current_sum
            elif current_sum < 0:
                i = j 
                break
            #if j has fully iterated the list w/out hitting the elif above, then there is no distinctive sub array and the evalution process is complete. i is advanced to prevent redundant loops and preserve runtime
            if j == len(array) -1:
                i = j 
                break
            j += 1
        i += 1
    #i stopping at one idx before len(array) -1 creates an edge case where, if the last value alone is the greatest subarray, it could be overlooked - the if below solves for that
    if array[-1] > greatest_sum:
        greatest_sum = array[-1]
    return greatest_sum

print(max_sub_sum([1,2,-4,3,-2,3,-1]))
#4
print(max_sub_sum([-1,-2,-4,-3,-2,-3]))
#0
print(max_sub_sum([1,2,-4,3,-2,3,-1,5]))
#8
print(max_sub_sum([-1,-2,-4,3,-2,5]))
#6
print(max_sub_sum([-1,2,-4,-3,-2,-3]))
#2
print(max_sub_sum([-1,2,-4,-3,-2,-3, 5]))
#5

