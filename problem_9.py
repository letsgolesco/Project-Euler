# Pythagorean triplet: a < b < c, a^2 + b^2 = c^2
# Find the triplet where a + b + c = 1000

# Start with first pythagorean triplet
# Increment b repeatedly
# If sqrt(c) is not an integer, increase b
# Else if a + b + c is less than 1000, increase b
# Else if a + b + c is greater than 1000, increase a, set b = a + 1, repeat

import math

a = 3
b = 4
c = 5

def is_round(n):
    if n == math.floor(n):
        return True
    else:
        return False

while True:
    c = math.sqrt(a*a + b*b)
    p_sum = a + b + c
    if is_round(c):
        if p_sum < 1000:
            b += 1
        elif p_sum > 1000:
            a += 1
            b = a + 1
        elif p_sum == 1000:
            p_product = a * b * c
            print "SOLUTION:"
            print "a = " + str(a)
            print "b = " + str(b)
            print "c = " + str(c)
            print "Product! " + str(p_product)
            break
    else:
        if p_sum < 1000:
            b += 1
        else:
            a += 1
            b = a + 1

# Solution without programming (from forums):
# a = 2mn; b = m^2; c = m^2 + n^2
# a + b + c = 1000
#
# 2mn + (m^2 - n^2) + (m^2 + n^2) = 1000
# 2mn + 2m^2 = 1000
# 2m(m+n) = 1000
# m(m+n) = 500
# m > n
# m = 20; n = 5
# a = 200; b = 375; c = 425
