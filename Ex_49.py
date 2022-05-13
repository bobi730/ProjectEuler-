# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways:
# (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.
#
# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property,
# but there is one other 4-digit increasing sequence.
#
# What 12-digit number do you form by concatenating the three terms in this sequence?

import math

l=list(range(0,10000))
primes=[]
def cull(l,num):
    for i in range(num,len(l),num):
        l[i]=0
for i in range(2,len(l)):
    if l[i]!=0:
        primes.append(l[i])
        cull(l,l[i])
primes=primes[168:]

def checkPrime(n):
    if n==1:
        return False
    if n==2:
        return True
    for i in range(2,math.ceil(n**(1/2)+1)):
        if n%i==0:
            return False
    return True

perm = []
def permutations(head, tail=''):
    if len(head) == 0:
       perm.append(tail)
    else:
        for i in range(len(head)):
            permutations(head[:i] + head[i+1:], tail + head[i])

POSSIBLE=[]
for p in primes:
    perm=[]
    permutations(str(p))
    flag=False
    br=0
    possible=[]
    for i in perm:
        if checkPrime(int(i))==True:
            br=br+1
            possible.append(int(i))
    if br>=3:
        flag=True
    if flag==True and len(set(possible))>=3:
        POSSIBLE.append(sorted(set(possible)))


for triple in POSSIBLE:
    n=len(triple)-2
    for i in range(0,n):
        for j in range(i+1,n+2):
            if (triple[j]+(triple[j]-triple[i])) in triple and len(str(triple[i]))==4:
                print((triple[i],triple[j],triple[j]+(triple[j]-triple[i])))
