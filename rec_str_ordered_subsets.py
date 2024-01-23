# String In-Order Subsets
# Create strSubsets(str)​. Return array with all
# possible in-order character subsets of str. The
# result array itself need not be in a specific order.
# Given "abc"​, return ["", "c", "b", "bc",
# "a", "ac", "ab", "abc"]

'''
base is 1 char -> append and return
for each letter in str do a recursive call on a str w/out that letter
last letter special treatment to avoid index issues
'''

def str_subsets(string:str):
    my_list = []
    length = len(string)
    my_list.append(string)
    if length <= 1:
        return my_list
    last = length - 1
    for i in range(length):
        if i == last:
            my_list.extend(str_subsets(string[:last]))
        else:
            txt = string[:i] + string[i + 1:]
            my_list.extend(str_subsets(txt))
    my_set = set(my_list)
    my_list = list(my_set)
    return my_list


print(str_subsets("abc"))
#['abc', 'c', 'ac', 'bc', 'ab', 'a', 'b']


print(str_subsets("abcdef"))
#['adef', 'def', 'cdef', 'acdef', 'abd', 'bdf', 'bcd', 'ac', 'abc',
# 'abce', 'acdf', 'abdef', 'bcf', 'ace', 'adf', 'bde', 'af', 'bdef', 'ade', 'ce',
# 'abcdef', 'bcdef', 'd', 'b', 'bd', 'ab', 'abde', 'be', 'abcde', 'bc', 'abe', 'ef', 'abcd', 'ad', 'cef', 'bcde', 'bcef', 'cde', 'abf', 'df', 'cd', 'ae', 'abef', 'abcef',
# 'bef', 'acf', 'aef', 'bce', 'f', 'abcf', 'abdf', 'cf', 'c', 'acde', 'bcdf', 'a', 'e', 'bf', 'de', 'abcdf', 'acd', 'cdf', 'acef']