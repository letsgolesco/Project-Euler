# Find largest product of 4 consecutive numbers in any direction

# Read in 20x20 array as matrix in numpy (just a 2D list really)
# Scan products in each direction:
# horizontal, vertical, forward diagonal, backward diagonal

# Debugging the scanner functions was the hardest (read: most tedious) part
# There's a lot of repeated code that I would ideally consolidate,
# though this way the solution is fairly readable
# Could combine the scanners into one or two functions,
# sacrificing readability with each futher consolidation

import numpy

# Load up our 20x20 matrix
m = numpy.loadtxt('data_11.txt', delimiter=' ')
matrix = numpy.matrix(m)

# Variable to hold the current solution
greatest_product = 0
# Constant for matrix length/width
MAX = 20

def scan_horizontal():
    global greatest_product
    for i in range(MAX):
        for j in range(MAX-3):
            new_product = 1
            for x in range(4):
                new_product *= matrix.item(i,j+x)
            if new_product > greatest_product:
                greatest_product = new_product

def scan_vertical():
    global greatest_product
    for j in range(MAX):
        for i in range(MAX-3):
            new_product = 1
            for x in range(4):
                new_product *= matrix.item(i+x,j)
            if new_product > greatest_product:
                greatest_product = new_product

def scan_forward_diagonal():
    global greatest_product
    for i in range(MAX-3):
        for j in range(MAX-3):
            new_product = 1
            for x in range(4):
                new_product *= matrix.item(i+x,j+x)
            if new_product > greatest_product:
                greatest_product = new_product

def scan_backward_diagonal():
    global greatest_product
    for i in range(3,MAX):
        for j in range(MAX-3):
            new_product = 1
            for x in range(4):
                new_product *= matrix.item(i-x,j+x)
            if new_product > greatest_product:
                greatest_product = new_product

scan_horizontal()
scan_vertical()
scan_forward_diagonal()
scan_backward_diagonal()
print greatest_product
