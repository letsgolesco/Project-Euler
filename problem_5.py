# First idea: increment up
# loop over each increment to check divisibility by 11 through 20 (1 to 10 covered therein)
# Second idea: Add numbers until divisible (never executed)

def is_good(n):
    for x in range(20,10,-1):
        if not is_divisible(n,x):
            return False
    return True

def find_answer(n):
    while not is_good(n):
        print n
        n += 20
    print n

def is_divisible(n,x):
    if (n%x == 0):
        return True
    else:
        return False

# find_answer(2520)

# Better way doesn't really require programming:
# 20 = 2^2 * 5
# 19 = 19
# 18 = 2 * 3^2
# 17 = 17
# 16 + 2^4
# 15 = 3 * 5
# 14 = 2 * 7
# 13 = 13
# 12 = 3 * 4
# 11 = 11
# Multiply the greatest power of each prime factor above
answer = 2^4 * 3^2 * 5 * 7 * 11 * 13 * 17 * 19
