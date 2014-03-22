# Factorial digit sum
# Find the sum of the digits in the number 100!
# (It's not exciting, the "!" is a factorial)
#
# This one's easy in python...
# Probably harder in lower level languages cause the number is huge
#
# Basically you just need to iterate over & add the digits of the result
# In a lower level language, you may need to do a little math trick to
# store each part of the number in a different variable...

import math

n = math.factorial(100)
count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]    # Digit histogram
s = 0                                     # Sum variable

# Add each digit to the count & shave it off
while n != 0:
    digit = n % 10          # Get last digit
    count[digit] += 1       # Add digit to count
    n = (n - digit) / 10    # Remove last digit

# Iterate over digit histogram to get sum
for i in range(10):
    s += count[i] * i

print s
