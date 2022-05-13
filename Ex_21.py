# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
#
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
# The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.

import math
def d(num):
    res=0
    for  i in range(1,math.floor(num/2)+1):
        if num%i==0:
            res=res+i
    return res

sum=0
for i in range(1,10000):
    if d(d(i))==i and i!=d(i) and d(i)<10000:
        sum=sum+i
print(sum)
#very inefficient