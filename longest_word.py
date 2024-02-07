# Longest Word
# Create a function that, given a string of words,
# returns the longest word. Example: given "Snap
# crackle pop makes the world go
# round!"​, return "crackle"​.
# Bonus:​ handle punctuation

def longest(string: str):
    l = ""
    tracker = 0 
    for i in range(len(string)):
        if string[i].isalpha() == False:
            word = string[tracker:i]
            if len(word) > len(l):
                l = word
            tracker = i +1
    if len(string[tracker:]) > len(l):
        return string[tracker:]
    return l 


print(longest("Snap crackle pop makes the world go round!"))
#crackle


