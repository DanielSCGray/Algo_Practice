# Parens Valid
# Create a function that, given an input string,
# returns a boolean whether parentheses in that
# string are valid. 
# Given input "y(3(p)p(3)r)s"​,
# return true. Given "n(0(p)3"​, return false​.
# Given "n)0(t(0)k"​, return false​.

def paren_validator(str):
    paren_count = 0
    for char in str:
        if char == '(':
            paren_count +=1
        elif char == ')':
            paren_count -= 1
        if paren_count < 0:
            return False
    if paren_count == 0:
        return True
    return False

print(paren_validator("y(3(p)p(3)r)s"))
#true
print(paren_validator("n(0(p)3"))
#false
print(paren_validator("n)0(t(0)k"))
#false