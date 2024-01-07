# Flatten
# Flatten a given array, eliminating nested and
# empty arrays. Do not alter the array; return a new
# one retaining the order. Given the array
# [1,[2,3],4,[]]​, return a new [1,2,3,4]​.

def flatten1(array):
    new_array = []
    for i in range(len(array)):
        if type(array[i]) == list:
            sub_arr = array[i]
            if len(sub_arr)>0:
                for j in range(len(sub_arr)):
                    new_array.append(sub_arr[j])
            else:
                continue
        else:
            new_array.append(array[i])
    return new_array


test = [1,[2,3],4,[]]
print(type(test)== list)

print(flatten1(test))
# [1,2,3,4]


# Second:​ Work ‘in-place’ in the given array (do
# not create another). Alter order if needed. Ex.:
# [1,[2,3],4,[]]​ could become [1,3,4,2]​.

def flatten2(array):
    for i in range(len(array)):
        if type(array[i]) == list:
            sub_arr = array[i]
            if len(sub_arr) > 0:
                for j in range(len(sub_arr)):
                    array.append(sub_arr[j])
            array.pop(i)
    return array
print(flatten2(test))
#[1,4,2,3]
print(test)


# Third:​ Make your algorithm both in-place and
# stable. Do you need a return value?

def flatten3(array):
    i = 0
    while i < len(array):
        if type(array[i]) == list:
            sub_arr = array.pop(i)
            if len(sub_arr) == 0:
                continue
            for num in sub_arr:
                array.insert(i, num)
                i+=1
        else:
            i+=1
    return array

test2 = [1,[2,3],4,[]]

flatten3(test2)
print(test2)
#[1, 2, 3, 4]           
