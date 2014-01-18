# Find the sum of the digits of the number 2^1000

num = 2**1000
string = str(num)
summation = 0

for i in string:
    summation += i

print summation

# Handling all the digits of 2^1000 would be a bigger problem in lower-level languages

# Nice python one-liner (from forums):
sum(int(digit) for digit in str(2**1000))
