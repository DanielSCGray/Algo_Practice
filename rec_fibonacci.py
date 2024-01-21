# Recursive Fibonacci
# Write rFib(num)​. Recursively compute and
# return the numth Fibonacci value. As earlier, treat
# the first two (num = 0, num = 1) Fibonacci values
# as 0 and 1. Thus, rFib(2)​ = 1 (0+1); rFib(3)
# = 2 (1+1); rFib(4)​ = 3 (1+2); rFib(5)​ = 5
# (2+3). Also, rFib(3.65)​ = rFib(3)​ = 2.
# Finally, rFib(-2)​ = rFib(0)​ = 0.

def r_fib(num):
    if num < 0:
        return 0
    if type(num) == float:
        num = int(num)
    if num <= 1:
        return num
    return (r_fib(num -1) + r_fib(num -2))

print(r_fib(4))
#3
print(r_fib(3))
#2
print(r_fib(3.4))
#2
print(r_fib(-2))
#0
