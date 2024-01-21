# Binary String Expansion
# You will be given a string containing characters
# ‘0’, ‘1’, and ‘?’. For every ‘?’, either ‘0’ or ‘1’
# characters can be substituted. Write a recursive
# function that returns an array of all valid strings
# that have ‘?’ characters expanded into ‘0’ or ‘1’.
# Ex.: binStrExpand("1?0?")​ should return
# ["1000","1001","1100","1101"]​. For this
# challenge, you can use string functions such as
# slice()​, etc., but be frugal with their use, as
# they are expensive.


#actually going to pseudo-code!

'''
base case str doesn't contain '?'
if hits then append to a list and return the list
else 
find ?, create 2 new strings with 0 and with 1 replacing
recursive call on these 2 new ones
join result to current list

return list

'''

def rbs_expand(string: str):
    my_list = []
    idx = string.find("?")
    if idx == -1:
        my_list.append(string)
        return my_list
    txt1 = string[:idx] + "0" + string[idx + 1:]
    txt2 = string[:idx] + "1" + string[idx + 1:]
    my_list.extend(rbs_expand(txt1))
    my_list.extend(rbs_expand(txt2))
    return my_list

print(rbs_expand("1?0?"))
#['1000', '1001', '1100', '1101']
print(rbs_expand("1???"))
#['1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111']