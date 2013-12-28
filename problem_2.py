# Fibonacci number method
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-2) + fib(n-1)

# Create set of even Fibonacci numbers where no value exceeds n
def fib_seq(n):
    x = 2
    sum = 0
    while True:
        new_fib = fib(x)
        if new_fib < n:
            x += 1
            if new_fib%2 == 0:
                sum += new_fib
        else:
            return sum

print fib_seq(4000000)

# Begoner on the thread had an interesting way to do it
# E + E = E (never happens); O + O = E; E + O = O
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144...
# O, O, E, O, O, E, O, O, E, O, O, E...
# In the Fibonacci sequence, every third number is even
# No need for modulo, no need to calculate the odd numbers either
# Starting with two odd terms x and y, the series is:
# x, y, x+y, x+2y, 2x+3y, 3x+5y...
# Begoner's function:
def calcE():
    x = y = 1
    sum = 0
    while (sum < 1000000):
        sum += (x + y)
        x, y = x + 2*y, 2*x + 3*y
    return sum
