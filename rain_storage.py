# Rain Terraces
# A store wants to sell excess water so it landscapes its
# rooftop with a set of unusual elevated terraces. They are all the same width, but have varying heights.
# When it rains, water gathers in low terraces that are surrounded by taller ones. For example, if we have
# terraces with heights [3,1,1,4,2]​, then as much as 4 units of water could be gathered, because
# water would pool 2-deep on two different terraces (both of the 1-high terraces: between the 3-high and
# 4-high terraces). Water on the other terraces just runs off. Given an array of terrace heights, return the
# maximum amount of water that is trapped when rains come.


def get_max_water(array):
    total_water = 0
    i = 0 
    #I use a while loop so I can advance the i var manually(python for loops don't allow this)
    while i < len(array)-1:
        if array[i] <= array[i+1]:
            i += 1
            continue
        j = i+1
        start_idx = i
        end_idx = i
        low_point = array[j]
        while j < len(array):
            if array[j] <= low_point:
                low_point = array[j]
                j +=1
                continue
            elif array[j] >= array[i]:
                end_idx = j
                break
            #hitting this else means array[i] > array[j] > low_point. we will check if this is the new highest right-side wall and update accordingly
            else:
                if end_idx == i:
                    end_idx = j
                    j+=1
                    continue
                if array[j] >= array[end_idx]:
                    end_idx = j
                j += 1
        #if the j loop terminated without finding a new end that means there is no more water to count
        if end_idx == start_idx:
            return total_water
        #find the shorter of the two outer walls
        if array[start_idx]> array[end_idx]:
            short_wall = array[end_idx]
        else:
            short_wall = array[start_idx]
        for k in range(start_idx+1, end_idx):
            total_water += (short_wall - array[k])
        #move i up to j in case the wall at j can be the left-wall of a new sub-array
        i = j
    return total_water

print(get_max_water([3,1,1,4,2]))
#4
print(get_max_water([1,1,1,4,2]))
#0
print(get_max_water([3,1,4,1,2]))
#3
print(get_max_water([3,1,1,1,0]))
#0
print(get_max_water([0,1,1,1,3]))
#0



