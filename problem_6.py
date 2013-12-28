# My way: brute force

sum_of_squares = 0
sums = 0
square_of_sum = 0

for x in range (101):
    print x
    sum_of_squares += x*x
    sums += x

square_of_sum = sums*sums

difference = sum_of_squares - square_of_sum

print "Sum is: " + str(sums)
print "Sum of squares is: " + str(sum_of_squares)
print "Square of sum is: " + str(square_of_sum)
print "Difference: " + str(difference)

# Smart way: use properties of series
# (1 + 2 + ... + 99 + 100)^2 = (101 * 50)^2
# 1^2 + 2^2 + 3^2 + ... + 99^2 + 100^2 = 100*1 + 99*3 + 98*5 + ... + 2*197 + 1*199
