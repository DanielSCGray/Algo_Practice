# Balance Point
# Write a function that returns whether the given array has a balance point between indices, where one
# side’s sum is equal to the other’s. Example: [1,2,3,4,10]​ → true​ (between indices 3 & 4), but
# [1,2,4,2,1]​ → false​.

def balance_point(array) -> bool:
    right_sum = sum(array)
    left_sum = 0
    for i in range(len(array)):
        if left_sum == right_sum:
            return True
        right_sum -= array[i]
        left_sum += array[i]
    return False

print(balance_point([1,2,3,4,10]))
#True
print(balance_point([1,2,4,2,1]))
#False
test = [1,2,3,4,10]
l = test[1:]
print(l)

# Balance Index
# Here, a balance point is on an index, not between indices. Return the balance index where sums are
# equal on either side (exclude its own value). Return -1 if none exist. Ex.: [-2,5,7,0,3]​ → 2​, but
# [9,9]​ → -1​.

def balance_index(array) -> int:
    if len(array) < 3:
        return -1
    for i in range(1, len(array)-1):
        left_side = array[:i]
        right_side = array[i+1:]
        if sum(left_side) == sum(right_side):
            return i
    return -1

print(balance_index([-2,5,7,0,3]))
#2
print(balance_index([9,9]))
#-1