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

def is_palindrome(str):
    right = len(str) -1 
    for i in range(len(str)):
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

