# Mode of Array
# Back in the Basic 13, you wrote code to compute
# an array’s minimum and maximum values. You
# also wrote code to determine average value (the
# “mean”). What about the “mode” – the most
# common value in that data set. Create a function
# that, given an array, returns the most frequent
# value in the array.
def mode_find(array):
    hash = {}
    for num in array:
        if num in hash.keys():
            hash[num] += 1
        else:
            hash[num] = 1
    mode = array[0]
    occurances = hash[mode]
    for key in hash.keys():
        if hash[key] > occurances:
            mode = key
            occurances = hash[key]
    return mode

test = [1,1,1,2,2,2,2,2,3,4,5,6,7,8,9,9,]
print(mode_find(test))
#2




# Second:​ if because of memory constraints you
# were forced to do this without creating a new
# array, how would it affect your solution?

#it would change the runtime to O(n^2) because of a nested loop

    