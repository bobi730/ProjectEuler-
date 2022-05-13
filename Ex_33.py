# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may
# incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
#
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
#
# There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing
# two digits in the numerator and denominator.
#
# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.


# Notation wrong, worked with it,otherwise sound.
import math
numerator=list(range(11,100))
for i in range(20,91,10):
    numerator.remove(i)
denominator=[]

for n in numerator:
    first=math.floor(n/10)
    second=n%10
    sameSecond=[]
    sameFirst=[]
    crissCrossF=[]
    crissCrossS=[]
    for a in range(1,first):
        sameSecond.append(a*10+second)
    for b in range(1,second):
        sameFirst.append(first*10+b)
    if second<=first:
        for b in range(1,10):
            crissCrossF.append(second*10+b)
        for a in range(1,first):
            crissCrossS.append(a*10+first)
    if second>first:
        for a in range(1,first+1):
            crissCrossS.append(a*10+first)
    denominator. append([sameFirst,sameSecond,crissCrossF,crissCrossS])

dcf=[]
for n in numerator:
    for d1 in denominator[numerator.index(n)][0]:
        if d1/n==(d1%10)/(n%10) and d1/n!=1:
            dcf.append([(d1%10),(n%10),d1,n])
    for d2 in denominator[numerator.index(n)][1]:
        if d2/n==math.floor(d2/10)/math.floor(n/10) and d2/n!=1:
            dcf.append([math.floor(d2/10),math.floor(n/10),d2,n])
    for d3 in denominator[numerator.index(n)][2]:
        if d3/n==(d3%10)/math.floor(n/10) and d3/n!=1:
            dcf.append([(d3%10),math.floor(n/10),d3,n])
    for d4 in denominator[numerator.index(n)][3]:
        if d4/n==math.floor(d4/10)/(n%10) and d4/n!=1:
            dcf.append([math.floor(d4/10),(n%10),d4,n])
print(dcf)
