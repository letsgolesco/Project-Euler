# Find the sum of all primes below 2 million
# My strategy: use the prime list building algo from before
# Stop the list building loop when you reach 2 million
# Sum all elements of the list

#summation = 2
#primes = [2]

#def is_prime(n):
    #for x in primes:
        #if n%x==0:
            #return False
    #return True

#for x in range(3,2000000,2):
    #if is_prime(x):
        #primes.append(x)
        #summation += x

#print summation

# Second attempt:
# Use Sieve of Eratosthenes:
# 1) Create a list of consecutive integers 2 through n
# 2) Initialize p = 2
# 3) Mark all multiples of p in the list
# 4) Set p to lowest non-marked number, repeat
summation = 0
primes = []
upper = 2000000

for x in range(0,upper):
    primes.append(True)

for i in range(2,upper):
    if primes[i]:
        summation += i
        for j in range(2*i,upper,i):
            primes[j] = False

print summation

# I was originally trying to do this by creating an array of numbers
# Then popping primes into a prime array and testing primality of numbers
# based on that array... then summing that array
#
# Thankfully this much quicker implementation was on stackoverflow
