# You are given the following information, but you may prefer to do some research for yourself.
#
# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

import math
def monthD(key):
    m= {
        1:0,
        2:31,
        3:59,
        4:90,
        5:120,
        6:151,
        7:181,
        8:212,
        9:243,
        10:273,
        11:308,
        12:338,
    }
    return m.get(key,0)
def isSunday (month,year):
    dayspast=(year-1901)*365 + math.floor((year-1901)/4)+monthD(month)
    if year&4==0 and month>=3:
        dayspast=dayspast+1
    if (dayspast+2)%7==0:
        return True
    else:
        return False

br=0
for month in range(1,13):
    for year in range(1901,2001):
        if isSunday(month,year)==True:
            br=br+1
print(br)