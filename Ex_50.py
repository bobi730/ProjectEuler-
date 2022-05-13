# The prime 41, can be written as the sum of six consecutive primes:
#
# 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.
#
# The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
#
# Which prime, below one-million, can be written as the sum of the most consecutive primes?

import math
l=list(range(0,500000))
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

i=546
j=1
flag=False
while flag==False:
    for k in range(0,j):
        if checkPrime(sum(primes[k:i]))==True:
            flag=True
            print(sum(primes[k:i]))
            print(k)
        if checkPrime(sum(primes[0:i-k]))==True:
            flag=True
            print(sum(primes[k:i]))
            print(-k)
    j=j+1

print(checkPrime(997651))
print(sum(primes[3:546]))