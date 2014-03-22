# Names scores
#
# File given: names.txt, containing over 5000 first names
# Begin by sorting the list into alphabetical order
# Then work out the alphabetical value for each name
# (sum of numbers corresponding to each letter)
# Multiply this value by its position in the sorted list
# That's the name score!
#
# What's the total of all name scores?

# Function to find namescore
def namescore(name, index):
    score = 0
    # Iterate over chars & sum their values
    for char in name:
        score += ord(char) - 64     # Use unicode value & shift so A = 1
    score *= index + 1              # Multiply by spot in list
    return score

# Read in names file
f = open('names.txt', 'r')
bigstr = f.readline().replace('"', '')    # Remove quotes
names = bigstr.split(',')                 # Comma split
names.sort()                              # Thank you based python

# Iterate over names & sum their namescores
total = 0
for j in range(len(names)):
    ns = namescore(names[j], j)
    total += ns

print total
