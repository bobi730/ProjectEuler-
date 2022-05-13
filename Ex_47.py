# The first two consecutive numbers to have two distinct prime factors are:
#
# 14 = 2 × 7
# 15 = 3 × 5
#
# The first three consecutive numbers to have three distinct prime factors are:
#
# 644 = 2² × 7 × 23
# 645 = 3 × 5 × 43
# 646 = 2 × 17 × 19.
#
# Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?

def primeFactors(n):
    i=2
    factors=[]
    while i**2<=n:
        if n%i>0:
            i=i+1
        else:
            n=n//i
            factors.append(i)
    if n>1:
        factors.append(n)
    return set(factors)

flag=False
i=2
br=0
while flag==False:
    if len(primeFactors(i))==4:
        br=br+1
    else:
        br=0
    if br==4:
        flag=True
        print(i-3)
    i=i+1