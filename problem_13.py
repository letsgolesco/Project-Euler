# Work out the first ten digits of the sum of the following
# one-hundred 50-digit numbers

# Seriously? I think this is an issue in low-level languages
# You'd have to use 'long' or 'double' instead of 'int'
# A math trick would become necessary, but even that trick isn't so tricky
# Adding the first 11 digits of each number would do it
# (12th digit on will only affect the 11th digit, and we only need 10)

f = open('data_13.txt', 'r')

summation = 0

for line in f:
    summation += int(line)

print summation
