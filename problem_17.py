# How many letters does it take to write out all the numbers
# from 1 to 1000 (inclusive?) in English
# Don't count hyphens or spaces
# Number string format: use 'and'
# eg: 342 = three hundred and forty-two

# Idea: use a number_to_word function
# Call this function on all numbers 1 to 1000
# On each result, count characters of the word string (letters only!)
# Letters only: could either strip out spaces & hyphens at the end
# OR don't even collect them in the string

def num_to_word(num):
    word = ''
    s = str(num)
    ones = int(s[-1])

    # Special case fo 1000
    if num == 1000:
        return 'one thousand'

    # Handle third digit
    if len(s) > 2:
        hundreds = int(s[0])
        word += singles[hundreds] + ' hundred'
        # Don't need any more if it's an even hundred
        if (num % 100 == 0):
            return word
        else:
            word += ' and '

    # Handle second digit
    if len(s) > 1:
        # `tens` is a misleading variable name
        # because it has both of the last two digits... my bad
        tens = int(s[-2:])

        if int(s[-2]) == 0:
            pass
        elif tens < 21:
            word += doubles[tens]
            return word
        else:
            word += doubles[tens - ones] + ' '

    # Handle first digit
    if ones != 0:
        word += singles[ones]

    return word

# Dictionary of { ints : words }
singles = { 1: 'one',
            2: 'two',
            3: 'three',
            4: 'four',
            5: 'five',
            6: 'six',
            7: 'seven',
            8: 'eight',
            9: 'nine' }

doubles = { 10: 'ten',
            11: 'eleven',
            12: 'twelve',
            13: 'thirteen',
            14: 'fourteen',
            15: 'fifteen',
            16: 'sixteen',
            17: 'seventeen',
            18: 'eighteen',
            19: 'nineteen',
            20: 'twenty',
            30: 'thirty',
            40: 'forty',
            50: 'fifty',
            60: 'sixty',
            70: 'seventy',
            80: 'eighty',
            90: 'ninety' }

string = ''
for i in range(1,1001):
    print num_to_word(i)
    string += num_to_word(i).replace(' ','')
print len(string)

# I didn't think of this.. but it makes sense (thanks forums):
# You can count the amount of letters in each commonly occuring string
#   and use the amount of times each of those strings occurs.
# You can then make a few main groups based on common frequencies.
#
# Some Java-ish pseudo code:
# one_to_nine = "onetwothreefourfivesixseveneightnine".length
# ten_to_nineteen = "teneleventwelvethirteenfourteenfifteensixteenseventeeneighteennineteen".length
# and = "and".length
# twenty_to_ninety = "twentythirtyfortyfiftysixtyseventyeightyninety".length
# hundred = "hundred".length
# thousand = "thousand".length
# one = "one".length
#
# count = one + thousand + (900 * hundred) + 100 * (one_to_nine + twenty_to_ninety)
#         + 891 * and + 80 * one_to_nine + 10 * (one_to_nine + ten_to_nineteen)
