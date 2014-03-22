# Counting Sundays
# You are given the following info:
# * 1 Jan 1900 was a Monday
# * Number of days in each month (thanks...)
# * Leap years occur on any year divisible by 4,
#   except centuries where they must be divisible by 400
#
# How many Sundays fell on the first of the month
# during the 20th century (1 Jan 1901 - 31 Dec 2000)?
#
# To change day of week index for each month:
#    Add month length % 7
# When day of week index is greater than 6:
#    Subtract 7

days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
                'Saturday', 'Sunday']

# The first day of 1901 was a Tuesday
day_index = 1       # Day of the 1st of the month
sunday_count = 0    # Our counter

# Iterate over years 1901-2000
for i in range(1901, 2001):
    # Figure out number of days in February for that year
    if ((i % 4 == 0) and (i % 100 != 0)) or (i % 400 == 0):
        days_per_month[1] = 29
    else:
        days_per_month[1] = 28

    # Iterate over the months of that year
    for j in range(12):
        inc = days_per_month[j] % 7    # Num of weekdays to increment by
        day_index += inc               # Increment weekday index
        if day_index > 6:
            day_index -= 7             # Handle wrap-around
        if day_index == 6:
            sunday_count += 1          # Sunday 1st, increment the count!

print sunday_the_firsts
