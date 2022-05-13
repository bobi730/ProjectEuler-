# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.
#
# What is the largest n-digit pandigital prime that exists?

import math
perm = []
def permutations(head, tail=''):
    if len(head) == 0:
       perm.append(tail)
    else:
        for i in range(len(head)):
            permutations(head[:i] + head[i+1:], tail + head[i])
permutations('1234567')

def checkPrime(n):
    if n==1:
        return False
    if n==2:
        return True
    for i in range(2,math.ceil(n**(1/2)+1)):
        if n%i==0:
            return False
    return True
top=0
for i in perm:
    if checkPrime(int(i))==True:
        if top<int(i):
            top=int(i)
print(top)