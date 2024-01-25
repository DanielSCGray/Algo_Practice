# Given the number of pairs of parentheses, return
# an array of strings, where each string represents
# a different valid way to order those parentheses.
# Example: given 2​, return ["()()", "(())"]​.

def parens(num):
    if num == 1:
        return ["()"]
    my_list = []
    num -= 1
    for formation in parens(num):
        for i in range(len(formation)):
            my_list.append(formation[:i] + "()" + formation[i:])
    my_list = set(my_list)
    my_list = list(my_list)
    return my_list

print(parens(2))
#['()()', '(())']
print(parens(3))
# ['()(())', '(()())', '()()()', '(())()', '((()))']

def parens2(num):
    if num == 1:
        return ["()"]
    my_list = []
    num -= 1
    for formation in parens(num):
        for i in range(len(formation)):
            combo = formation[:i] + "()" + formation[i:]
            if not combo in my_list:
                my_list.append(combo)
    return my_list

print(parens2(2))
#['()()', '(())']
print(parens2(3))
# ['()()()', '(())()', '()(())', '(()())', '((()))']