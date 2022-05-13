# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c},
# there are exactly three solutions for p = 120.
#
# {20,48,52}, {24,45,51}, {30,40,50}
#
# For which value of p ≤ 1000, is the number of solutions maximised?

import math
def numTr(num):
    br=0
    top=math.ceil(num/(2+2**(1/2)))
    for i in range(1,top):
        if (((num**2)-2*i*num)/(num-i))%1==0:
            br=br+1
    return br

max=0
p=0
for num in range(1,1001):
    a=numTr(num)
    if max < a:
        max=a
        p=num

print((max,p))
