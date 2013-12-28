# Find the largest palindrome made from the product of two 3-digit numbers
# My idea:
# Starting at 999, check every product with decrementing integers (999, 998, 997...)
# The first one that makes a palindrome is the minimum possible factor
# Continue the same process for 998, 997... until min
# Each iteration, store the new palindrome if it is higher

# Notes:
# Highest 3-digit number: 999
# Lowest 3-digit number : 100

#Global variable to track our minimum possible factor
min = 100

# Function to check whether number is palindrome
def is_palindrome(n):
    num_str = str(n)
    half = len(num_str) / 2
    first_half = num_str[:half]
    second_half = num_str[-half:]
    reverse_second_half = second_half[::-1]
    if first_half == reverse_second_half:
        return True
    else:
        return False

def find_first_palindrome(num):
    global min
    i = num
    pal = 0
    while not is_palindrome(pal):
        pal = num*i
        i -= 1
        if i < min:
            return 0
    if num == 999:
        min = i
    return pal

def find_highest_palindrome():
    global min
    cur_pal = 0
    max = 999
    x = max
    while x > min:
        new_pal = find_first_palindrome(x)
        if new_pal > cur_pal:
            cur_pal = new_pal
        x -= 1
    return cur_pal

print find_highest_palindrome()

typed_input = str(input("Type something:"))
print "your input was: " + typed_input
