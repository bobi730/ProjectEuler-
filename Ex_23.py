# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
# For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
#
# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
#
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two
# abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written
# as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it
# is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
#
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

import math
def d(num):
    res=0
    for  i in range(1,math.floor(num/2)+1):
        if num%i==0:
            res=res+i
    return res
abundant=[]
for i in range(0,28112):
    if d(i)>i:
        abundant.append(i)
doubleAbundant=[]
for a in abundant:
    for b in abundant:
        if a+b<=28123:
            doubleAbundant.append(a+b)
doubleAbundant=set(doubleAbundant)
dA=list(doubleAbundant)
total=0
i=0
current=0
while i<len(dA):
    top=dA[i]
    while current<top:
        total=total+current
        current=current+1
    current=current+1
    i=i+1
print(total)

#very very inefficient