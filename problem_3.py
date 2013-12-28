# Iterate i from 2 to square root of n
# If n is divisible by i, divide n by i
# Otherwise, increment i

tall = 600851475143

def highest_prime_factor(n):
    i = 2
    while i*i < n:
        while n%i == 0:
            n /= i
        i += 1
    return n

print highest_prime_factor(tall)

# Not proud, I had to google a lot and eventually just found this solution...
# Learned about the Sieve of Eratosthenes though, very cool
