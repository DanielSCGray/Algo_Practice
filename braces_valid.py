# Braces Valid
# Given a string, returns whether the sequence of
# various parentheses, braces and brackets within
# it are valid. For example, given the input string
# "w(a{t}s[o(n{c}o)m]e)h[e{r}e]!"​, return
# true​. Given "d(i{a}l[t]o)n{e"​, return
# false​. Given "a(1)s[O(n]0{t)0}k"​, return
# false​.

def validator(str):
    # my approach will use a stack to track the opening characters and then compare to the closers to ensure all are valid
    opener_stack = []

    for char in str:
        if char in ['(', '[', '{']:
            opener_stack.append(char)
        
        elif char in [')', ']', '}']:
            if len(opener_stack) == 0:
                #if we hit a closer and the opener stack is empty it must be invalid
                return False
            temp_opener = opener_stack.pop()
            #the "top" opener on the opener stack will be popped and checked against the current closer. if they fit the loop will continue; if not it is invalid and we return false 
            if temp_opener == '(':
                if char != ')':
                    return False
            if temp_opener == '[':
                if char != ']':
                    return False
            if temp_opener == '{':
                if char != '}':
                    return False
    if len(opener_stack) > 0:
    #any remaining openers indicate an unclosed expression which is invalid
        return False
    return True

print(validator("w(a{t}s[o(n{c}o)m]e)h[e{r}e]!"))

print(validator("d(i{a}l[t]o)n{e"))

print(validator("a(1)s[O(n]0{t)0}k"))