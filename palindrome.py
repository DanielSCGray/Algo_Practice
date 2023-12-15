# Strings like "Able was I, ere I saw
# Elba"​ or "Madam, I'm Adam"​ could be
# considered palindromes, because (if we ignore
# spaces, punctuation and capitalization) the letters
# are the same from front and back.
# Create a function that returns a boolean whether
# the string is a strict palindrome. For "a x a"​ or
# "racecar"​, return true​. Do not​ ignore spaces,
# punctuation and capitalization: if given "Dud"​ or
# "oho!"​, return false

#pretty simple: will check string from the outside-in. if the midpoint is reached with no discrepancies we can return True. Runtime O(n) => O(n/2) is more accurate but technically incorrect for big O
def is_palindrome(str):
    right = len(str) -1 
    mid_point = len(str) //2
    for i in range(mid_point):
        if str[i] != str[right]:
            return False
        right -=1
    return True

print(is_palindrome("a x a"))
#True
print(is_palindrome("racecar"))
#True
print(is_palindrome("Dud"))
#False

