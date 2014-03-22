# Non-abundant sums
#
# A number n is a perfect number if n = the sum of its proper divisors
# eg: 1 + 2 + 4 + 7 + 14 = 28
#
# n is 'deficient' if the sum of its proper divisors is less than n
# n is 'abundant' if the sum of its proper divisors is greater than n
#
# 12 is the smallest abundant number: 1 + 2 + 3 + 4 + 6 = 16
# 24 is the smallest number that can be written as the sum of two
# abundant numbers
# All integers greater than 28123 can be written as the sum of two
# abundant numbers
#
# Find the sum of all the positive integers which cannot be written as
# the sum of two abundant numbers
#
# Okay... so for this one, I'm thinking we need to find all abundant
# numbers under 28123.
# Then we need to (kind of) iterate over every number under 28123 and
# eliminate those which can be written as the sum of two abundants...

import math
import time
start = time.time()
# Function to find whether n is abundant
def is_abundant(n):
    total = 0
    # Find all proper divisors
    for x in range(1, int(math.sqrt(n)) + 1):
        if n % x == 0:
            total += x
            if x != 1 and x != n / x:
                total += n / x
    return total > n

# dat list comprehension
abundants = [i for i in range(12, 28124) if is_abundant(i)]
total = 0

# Iterate through positive integers under 28124
for n in range(1, 28124):
    can = False    # Boolean: is n sum of two abundants?
    for x in abundants:
        if x >= n:
            # Break when you reach an abundant greater than n
            break
        if is_abundant(n - x):
            # If n - x = an abundant, break & don't add it to the sum
            can = True
            break
    if not can:
        # If n isn't the sum of abundants, add it to the sum
        total += n

print total
print time.time()-start

# This solution works, but it's pretty slow...
