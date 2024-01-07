# Remove Duplicates
# Remove duplicates from an array. Do not alter
# the original array; return a new one, keeping
# results ‘stable’ (retain original order). Given [1, 2,
# 1, 3, 4, 2], return a new array [1, 2, 3, 4].

def dup1(array):
    tracker = []
    for num in array:
        if num in tracker:
            continue
        tracker.append(num)
    return tracker

print(dup1([1, 2, 1, 3, 4, 2]))
#[1, 2, 3, 4]

# Second:​ Work ‘in-place’ in given array. Alter
# order if needed (stability is not required). Ex.:
# [1,2,1,3,4,2]​ could become [1,2,4,3]​.

def dup2(array):
    i = 0 
    while i < len(array)-1:
        number = array[i]
        j = i +1
        while j < len(array):
            if number == array[j]:
                array.pop(j)
                continue
            j += 1
        i += 1
    return array


print(dup2([1, 2, 1, 3, 4, 4, 2]))
# [1, 2, 3, 4]

# Third:​ Make it in-place and stable.

#above is stable

# Fourth:​ Can you make this faster by eliminating
# any second inner loop?

#yes, can use a second tracking array for a linear big O runtime
