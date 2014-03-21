# Maximum path sum 1
# Find the maximum total from top to bottom of the given triangle
#
# Though it says top-to-bottom, a better way to do this is bottom-to-top
# Rather than brute-forcing every possible path from top-to-bottom,
# we can start at the bottom and sum up each 3-number triangle
#
# Sum every number in the 2nd last row with the larger of its two children
# Repeat until you reach the top
# BOOM DONE


# This will be our "triangle"
t = []

# Read numbers from the file into a 2D list
f = open('data_18', 'r')
for line in f:
    tmp = []
    for numstr in line.split(' '):
        tmp.append(int(numstr))
    t.append(tmp)

# Iterate from the 2nd last row to the top
for i in range(1, len(t)):
    row = len(t) - 1 - i
    # Iterate through all numbers in the row
    for j in range(len(t[row])):
        # Increment each number by the value of its largest child
        t[row][j] += max(t[row+1][j], t[row+1][j+1])

print t[0][0]
