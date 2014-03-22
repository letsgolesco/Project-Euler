# Amicable Numbers
#
# Let d(n) = the sum of the proper divisors of n
# (proper divisor being all positive divisors less than n)
#
# Given a and b, if d(a) = b and d(b) = a, a and b are an amicable pair
# eg: d(220) = 284 and d(284) = 220
#
# Evaluate the sum of all amicable numbers under 10000
#
# I just iterated over every number from 1 to 10000,
# found the sum of their divisors,
# and checked whether the sum of that sum's divisors
# was equal to that number
# Basically: find d(a) = b, then whether d(b) = a && a != b
# If the condition is met, a & b are added to the amicable list
# Then, the amicable list's elements are summed

import math

amicable = []

# Function to find sum of divisors of n
def d(n):
    total = 0
    # Find all the low divisors by iterating up to the square root
    for x in range(1, int((math.sqrt(n)))):
        # If divisor, add it to the total
        if n % x == 0:
            total += x
            # If divisor isn't 1, add its pair divisor if it's different
            if x != 1 and x != n / x:
                total += n / x
    return total

for a in range(1, 10000):
    if a not in amicable:
        b = d(a)
        if d(b) == a and a != b:
            amicable.append(a)
            amicable.append(b)

print sum(amicable)

# Wasn't really sure what's more efficient between
# storing amicable pairs in a list to prevent double-checking,
# or just adding 'a' and finding its 'b' again later in the loop
