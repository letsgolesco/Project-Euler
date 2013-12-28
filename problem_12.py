# Problem: find the first triangle number with over 500 divisors

# Brute force solution:
# Continuously generate triangle numbers
# For each, find/count all divisors
# Stop when the count reaches 500

# There's got to be a mathematically smarter way to do this...
# Cool pattern I noticed:
# 1:   1  *  1
# 3:   1  *  3
# 6:   2  *  3
# 10:  2  *  5
# 15:  3  *  5
# 21:  3  *  7
# 28:  4  *  7
# 36:  4  *  9
# 45:  5  *  9
# 55:  5  *  11
# Starting from 1:
# Left factor increases by 1 on every even iteration
# Right factor increases by 2 on every odd iteration

# Brute force attempt:
import math

triangle = 0
i = 0
while True:
    i += 1
    triangle += i
    divisors = []

    # We only need to find divisors up to the square root
    # From these divisors we can find all those above the square root
    # (for what it's worth I figured this out on my own)
    sqrt_floor = int(math.sqrt(triangle))
    for x in range(1,sqrt_floor+1):
        if triangle % x == 0:
            divisors.append(x)
            n = triangle/x
            if x != n:
                divisors.append(n)
    if len(divisors) >= 500:
        print triangle
        print len(divisors)
        break

# Brute force worked pretty quickly
# Interestingly large time difference between >=400 divisors and >=500 divisors

# The smart way to do this is as such (from forums):
# Let d(n) = number of divisors for n
# Find prime factors of n, such that: n = (p^a)(q^b)(r^c)...
# The number of divisors d(n) = (a+1)(b+1)(c+1)...
# (this can be proven, trust me...)
# Prime factors seem to be a recurring theme in these problems
