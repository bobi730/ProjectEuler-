# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
#
# Note: As 1! = 1 and 2! = 2 are not sums they are not included.

def f(key):
    fac= {
        0:1,
        1:1,
        2:2,
        3:6,
        4:24,
        5:120,
        6:720,
        7:5040,
        8:40320,
        9:362880,
    }
    return fac.get(key,0)
digF=[]
for n in range(0,3265921):
    s=str(n)
    l=len(s)
    add=0
    for d in range(0,l):
        add=add+f(int(s[d]))
    if add==n:
        digF.append(n)
digF.remove(1)
digF.remove(2)
print(digF)
print(sum(digF))