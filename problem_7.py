primes = [2]
test = 3
is_prime = False

def is_prime(n):
    for x in primes:
        if n%x==0:
            return False
    return True

def find_answer(n):
    global test
    while len(primes) < n:
        if is_prime(test):
            primes.append(test)
        test += 1
    return primes[-1]

print find_answer(10001)
print len(primes)
