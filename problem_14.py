# Find starting number under 1 million
# which produces the longest Collatz chain

def collatz(n):
    sequence = []
    while n > 1:
        sequence.append(n)
        if n % 2 == 0:
            n /= 2
        else:
            n = 3*n + 1
    return len(sequence)

longest = 0
starting_num = 0

for x in range(800001,1000000,2):
    new_length = collatz(x)
    if new_length > longest:
        longest = new_length
        starting_num = x

print longest
print starting_num

# This solution is terrible but it works
# Brute force, make collatz sequences for each number in a range under 1 million
# On a whim decided to start by checking from 800000
# Answer was 837799, with a chain 524 numbers long
# Also decided with little evidence that the starting number would be odd
# (made sense to me that starting with an increase would provide at least 1 more iteration)
# The good thing is, it only takes a few seconds...

# A little memoization idea from the foroum:
# Keep a hash table of previous chain lengths.
# If your current sequence reaches a number for which you've already found the chain length,
# add that calculated length to your current length for the current iteration
