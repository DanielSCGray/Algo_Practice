# Matrix Search
# You will be given 2 different two-dimensional arrays, containing integers between 0 and 65535. Each
# two-dimensional array represents a black-and-white image, where each integer value is a pixel value.
# The second matrix might be a subset of the larger one. Return whether the second image is found
# within the larger one.

    #building a helper to make my matricies
import random

def rand_num_list_gen(low,high,length):
    rand_list = []
    for i in range(length):
        num = random.randint(low, high)
        rand_list.append(num)
    print(f"{rand_list},")
    return rand_list

    #the second one would have to exist in it's entirity to count as being found in the first
    #this means I can limit the range of the search in image 1 

def matrix_search(large_matrix, small_matrix):
    #get the height and width of small matrix
    sm_height = len(small_matrix)
    sm_width = len(small_matrix[0])
    sm_start = small_matrix[0][0]
    for i in range(len(large_matrix)-sm_height + 1):
        lm_row = large_matrix[i]
        for j in range(len(large_matrix[i])-sm_width + 1):
            if lm_row[j] == sm_start:
                lm_row_idx = i
                lm_col_idx = j
                match = True
                for sm_row in small_matrix:
                    if match == False:
                        break
                    for k in range(sm_width):
                        if sm_row[k] == large_matrix[lm_row_idx][lm_col_idx]:
                            lm_col_idx += 1
                        else:
                            match = False
                            break
                    lm_row_idx += 1
                    lm_col_idx = j
                if match == True:
                    return True
    return False


# for i in range(10):
#     rand_num_list_gen(1,9,10)
#ran the above then copy pasted the console output into var test_larger below

test_larger = [
[2, 4, 6, 5, 5, 9, 6, 6, 9, 5],
[4, 5, 1, 2, 7, 9, 3, 4, 8, 4],
[8, 2, 3, 2, 7, 3, 5, 9, 7, 3],
[8, 3, 6, 5, 2, 7, 3, 9, 5, 8],
[8, 1, 7, 9, 2, 5, 9, 5, 5, 6],
[9, 7, 5, 8, 8, 3, 7, 9, 5, 1],
[9, 3, 1, 6, 3, 1, 6, 2, 5, 5],
[8, 2, 8, 8, 3, 5, 6, 9, 1, 8],
[1, 9, 1, 6, 1, 4, 5, 8, 1, 8],
[4, 9, 4, 8, 3, 9, 6, 5, 8, 2]
]
#created the below from a section of test_larger should be true
test_smaller_1 = [
    [5, 2, 7, 3, 9],
    [9, 2, 5, 9, 5],
    [8, 8, 3, 7, 9],
    [6, 3, 1, 6, 2]
]

# for i in range(5):
#     rand_num_list_gen(1,9,5)

#ran the above to create smaller 2 which should be false
test_smaller_2 = [
[2, 5, 6, 5, 4],
[5, 2, 6, 7, 2],
[9, 4, 4, 8, 3],
[9, 4, 8, 5, 8],
[8, 4, 9, 6, 5]
]

#3rd test to see if a sub array at the bottom of test-larger still returns true
test_smaller_3 = [
    [8, 3, 5],
    [6, 1, 4],
    [8, 3, 9]
]

print(matrix_search(test_larger, test_smaller_1))
#true
print(matrix_search(test_larger, test_smaller_2))
#false
print(matrix_search(test_larger, test_smaller_3))
#true