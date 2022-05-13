# Euler discovered the remarkable quadratic formula:
#
#
# It turns out that the formula will produce 40 primes for the consecutive integer values .
# However, when  is divisible by 41, and certainly when  is clearly divisible by 41.
#
# The incredible formula  was discovered, which produces 80 primes for the consecutive values .
# The product of the coefficients, −79 and 1601, is −126479.
#
# Considering quadratics of the form:
#
# , where  and
#
# where  is the modulus/absolute value of
# e.g.  and
# Find the product of the coefficients,  and , for the quadratic expression that produces the maximum number of primes
# for consecutive values of , starting with .

#Extremely inefficient!!!

import math
l=list(range(0,2001000))
primes=[]
def cull(l,num):
    for i in range(num,len(l),num):
        l[i]=0
for i in range(2,len(l)):
    if l[i]!=0:
        primes.append(l[i])
        cull(l,l[i])


# def checkPrime(n):
#     for i in range(2, math.ceil(n**(1/2))):
#         if n % i == 0:
#             return False
#     return True

B=primes[:168]
aa=0
bb=0
res=0
maxprimes=0
for b in B:
    A = []
    i=0
    pr=primes[i]
    while pr-b-1<1000 and i<len(primes)-1:
        razlika = pr -b-1
        A.append(razlika)
        i=i+1
        pr=primes[i]
    for a in A:
        primes_test = []
        n = 0
        num = n ** 2 + a * n + b
        # while checkPrime(num)==True:
        while primes.count(num)>0:
            primes_test.append(num)
            n = n + 1
            num = n ** 2 + a * n + b
        if maxprimes<len(primes_test):
            maxprimes=len(primes_test)
            res=a*b
            aa=a
            bb=b
print(res,maxprimes,aa,bb)


