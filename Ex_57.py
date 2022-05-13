# In the first one-thousand expansions, how many fractions contain a numerator with more digits than the denominator?

def expand(b,a):
    return(a,2*a+b)

br=0
for i in range(1,1000):
    res = expand(1, 2)
    for j in range(0,i):
        res=expand(res[0],res[1])
    res=(res[1]+res[0],res[1])
    res=sorted(res)
    if len(str(res[0]))<len(str(res[1])):
        br=br+1

print(br)