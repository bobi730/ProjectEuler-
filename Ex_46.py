# It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.
#
# 9 = 7 + 2×12
# 15 = 7 + 2×22
# 21 = 3 + 2×32
# 25 = 7 + 2×32
# 27 = 19 + 2×22
# 33 = 31 + 2×12
#
# It turns out that the conjecture was false.
#
# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?


import math
def checkPrime(n):
    if n==1:
        return False
    if n==2:
        return True
    for i in range(2,math.ceil(n**(1/2)+1)):
        if n%i==0:
            return False
    return True

flag=True
i=9
while flag==True:
    if checkPrime(i)==True:
        i=i+2
    fl=False
    j=1
    while 2*(j**2)<i:
        if checkPrime(i-2*(j**2))==True:
            fl=True
        j=j+1
    if fl==False:
        print(i)
        flag=False
    i=i+2