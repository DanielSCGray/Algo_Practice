# rSigma
# Write a recursive function that, given a number,
# returns the sum of integers from one up to that
# number. For example, rSigma(5) = 1+2+3+4+5 =
# 15; rSigma(2.5) = 1+2 = 3; rSigma(-1) = 0.

def rec_sigma(num):
    if type(num) == float:
        num = num // 1
    if num < 1:
        return 0 
    sum = num 
    sum += rec_sigma(num-1)
    return sum

print(rec_sigma(5))
#15
print(rec_sigma(2.5))
#3
print(rec_sigma(6))
#21
print(rec_sigma(-1))
#0
