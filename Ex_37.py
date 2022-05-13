# The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits
# from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left:
# 3797, 379, 37, and 3.
#
# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
#
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

import math
l=list(range(0,1000000))
primes=[]
def cull(l,num):
    for i in range(num,len(l),num):
        l[i]=0
for i in range(2,len(l)):
    if l[i]!=0:
        primes.append(l[i])
        cull(l,l[i])

def checkPrime(n):
    if n==1:
        return False
    if n==2:
        return True
    for i in range(2,math.ceil(n**(1/2)+1)):
        if n%i==0:
            return False
    return True

def leftT(num):
    s=str(num)
    flag=True
    for i in range(0,len(s)):
        if checkPrime(int(s[i:]))==False:
            flag=False
    return flag

def rightT(num):
    s=str(num)
    flag=True
    for i in range(1,len(s)):
        if checkPrime(int(s[:i]))==False:
            flag=False
    return flag

sum=0
for item in primes[4:]:
    if leftT(item) and rightT(item):
        sum= sum+item
       # print(item)

print(sum)