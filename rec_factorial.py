# rFactorial
# Given a number, return the product of integers from 1 upward to that number. If less than zero, treat as
# zero. If not an integer, treat as an integer. Mathematicians tell us that 0! is equal to 1, so make
# rFact(0)​ = 1. Examples: rFact(3)​ = 6 (1*2*3). Also, rFact(6.5)​ = 720 (1*2*3*4*5*6).


def r_factorial(num):
    if type(num) == float:
        num = int(num)
    if num <= 1:
        return 1
    sum = num
    return sum * r_factorial(num -1)

print(r_factorial(3))
#6
print(r_factorial(0))
#1
print(r_factorial(6.5))
#720
print(r_factorial(10))
#3628800