# Write a function that given a sorted array of page
# numbers, return a string representing a book
# index. Combine consecutive pages to create
# ranges. Given [1, 3, 4, 5, 7, 8, 10]​,
# return the string "1, 3-5, 7-8, 10"​.

def index_maker(nums):
    index_string = ""
    j = -1
    #Python for loops dont allow us to change the iterating variable w/in the loop so the j weirdness is a work around. Could also re-write using a while loop. will actually do that for more practice.
    for i in range(len(nums)):
        if i <= j:
                continue
        if nums[i] == nums[-1]:
            index_string += str(nums[i])
            break
        if nums[i+1] != nums[i] +1:
            index_string += f"{nums[i]}, "
        if nums[i] +1 == nums[i+1]:
            index_string += f"{nums[i]}-"
            j=i
            while j+1 < len(nums):
                if nums[j+1] == nums[j] + 1:
                    j +=1
                else:
                    break
            i = j 
            if nums[i] == nums[-1]:
                index_string += str(nums[i])
                break
            index_string += f"{nums[i]}, "
    return index_string

print(index_maker([1, 3, 4, 5, 7, 8, 10]))
#1, 3-5, 7-8, 10
print(index_maker([1, 3, 4, 5, 7, 8, 9, 10]))
#1, 3-5, 7-10

def index_maker_with_a_while_loop(nums):
    index_string = ""
    i = 0 
    while i <len(nums):
        if nums[i] == nums[-1]:
            index_string += str(nums[i])
            break
        if nums[i+1] != nums[i] +1:
            index_string += f"{nums[i]}, "
        if nums[i] +1 == nums[i+1]:
            index_string += f"{nums[i]}-"
            j=i
            while j+1 < len(nums):
                if nums[j+1] == nums[j] + 1:
                    j +=1
                else:
                    break
            i = j 
            if nums[i] == nums[-1]:
                index_string += str(nums[i])
                break
            index_string += f"{nums[i]}, "
        i +=1
    return index_string

print(index_maker_with_a_while_loop([1, 3, 4, 5, 7, 8, 10]))
#1, 3-5, 7-8, 10
print(index_maker_with_a_while_loop([1, 3, 4, 5, 7, 8, 9, 10]))
#1, 3-5, 7-10