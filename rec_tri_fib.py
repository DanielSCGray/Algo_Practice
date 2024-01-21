# Recursive “Tribonacci”
# Write a function rTrib(num)​ that mimics the
# Fibonacci sequence, but adds the previous three
# values instead of the previous two values.
# Consider the first three (num = 0, num = 1, num =
# 2) Tribonacci numbers to be 0, 0 and 1. Thus,
# rTrib(3)​ = 1 (0+0+1); rTrib(4)​ = 2 (0+1+1);
# rTrib(5)​ = 4 (1+1+2); rTrib(6)​ = 7 (1+2+4).
# Handle negatives and non-integers appropriately
# and inexpensively.

def tribonacci(num):
    if type(num) == float:
        num = int(num)
    if num <= 1:
        return 0
    if num == 2:
        return 1
    return (tribonacci(num -3) + tribonacci(num -2) + tribonacci(num -1))

print(tribonacci(3))
#1
print(tribonacci(4))
#2
print(tribonacci(5))
#4
print(tribonacci(6))
#7