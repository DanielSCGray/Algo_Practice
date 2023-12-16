# Longest Palindrome
# For this challenge, we will look not only at the
# entire string, but also substrings within it.
# For a string, return the longest palindromic
# substring. Given "what up, dada?"​, return
# "dad"​. Given "not much"​, return "n"​. Include
# spaces as well (i.e. be strict, as in the “Is
# Palindrome” challenge): given "My favorite
# racecar erupted!"​, return "e racecar e"​.

#

def longest_pal(str):
    midpoint = len(str) // 2
    #instructions say return the first letter if no pal is found so that is set up as the initial values below:
    current_longest = str[0]
    current_len = 1
    #we start at the midpoint and expand out, then continue moving left:
    for i in range(midpoint, 0, -1):
        j = i - 1
        k = i + 1
        while str[j] == str[k]:
            j -= 1 
            k += 1 
            #index error prevention:
            if j <0 or k >= len(str):
                break
        if k - j -1 > current_len:
            #if we have found a longer palindrome, we update the variables storing the longest one and its length
            current_longest = str[j +1: k]
            current_len = len(current_longest)
    #repeat the process, now moving to the right
    for i in range(midpoint, len(str)-1):
        j = i - 1
        k = i + 1
        while str[j] == str[k]:
            j -= 1 
            k += 1 
            if j <0 or k >= len(str):
                break
        if k - j -1 > current_len:
            current_longest = str[j +1: k]
            current_len = len(current_longest)
    return current_longest

print(longest_pal("My favorite racecar erupted!"))
# e racecar e
print(longest_pal("racecar"))
# racecar
print(longest_pal("what up, dada?"))
# dad