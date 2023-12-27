# Common Suffix
# When given an array of words, returns the largest
# suffix (word-end) that is common between all
# words. For example, for input ["ovation",
# "notation", "action"]​, return "tion"​.
# Given ["nice", "ice", "sic"]​, return ""​.

#will find the shortest word in the list and then determine the common suffix by comparing characters 
#(if the shortest word is contained in its entirety by all others it will be considered a suffix even though it may not meet the linguistic definition of suffix)

def suffix_search(word_list):
    #could use sorted(word_list, key=len) but sorting the entire list is inefficient O(n*logn) when we only need the shortest
    common_suff = ""
    shortest_word = word_list[0]
    for word in word_list:
        if len(word) < len(shortest_word):
            shortest_word = word
    #we will use Python's negative indexing to search for common characters from back to front
    for i in range(-1, -len(shortest_word)-1, -1):
        is_common = True
        for word in word_list:
            if word[i] != shortest_word[i]:
                is_common = False
                break
        if is_common:
            common_suff = shortest_word[i:]
        else:
            return common_suff
    return common_suff

print(suffix_search(["ovation", "notation", "action"]))
#tion
print(suffix_search(["nice", "ice", "sic"]))
#""
print(suffix_search(["nice", "ice", "spice", "slice"]))
#ice
