# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
#
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
#
# How many circular primes are there below one million?

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
    for i in range(2,math.ceil(n**(1/2))):
        if n%i==0:
            return False
    return True

def circular(num):
    circle=[]
    l=len(num)
    for i in range(0,l):
        num=num[1:]+num[:1]
        circle.append(num)
    return circle
CP=[]
for num in primes:
   # print(num)
    numS=str(num)
    circle=circular(numS)
    flag=1
    for c in circle:
        if checkPrime(int(c))==False:
            flag=0
    if flag==1:
        for c in circle:
            CP.append(int(c))

#print(sorted(set(CP)))
print(len(set(CP)))