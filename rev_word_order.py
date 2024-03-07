# Reverse Word Order
# Create a function that, given a string of words
# (with spaces), returns new string with words in
# reverse sequence. Given "This is a test"​,
# return "test a is This"​.




def rev_word(string):
    s = ""
    tracker = len(string)
    for i in range(len(string) -1, -1, -1):
        if string[i] == " ":
            s += string[i : tracker]
            tracker = i
    s += " " + string[:tracker]
    return s

print(rev_word("This is a test"))




# Bonus:​ handle punctuation and capitalization.
# Example: given "Life is not a drill, go
# for it!"​ you should return "It for go,
# drill a not is life!"

def ssecond_versionnn(string: str):
    container = []
    s = ""
    tracker = len(string)
    for i in range(len(string) -1, -1, -1):
        if 