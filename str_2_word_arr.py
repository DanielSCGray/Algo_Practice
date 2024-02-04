# String2WordArray
# Given a string of words (with spaces, tabs and
# linefeeds), returns an array of words. Given
# "Life is not a drill!"​ return ["Life",
# "is" "not", "a", "drill!"]​.
# Bonus:​ handle punctuation.


def string_changer (string):
    my_list = []
    tracker = 0
    for i in range(len(string)):
        if string[i] == " ":
            my_list.append(string[tracker:i])
            tracker = i + 1
    my_list.append(string[tracker:])
    return my_list

print(string_changer("Life is not a drill!"))
#['Life', 'is', 'not', 'a', 'drill!']
