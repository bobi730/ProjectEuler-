# Combinatoric selections
# How many, not necessarily distinct, values of n over r
#  for 1<=n<=100, are greater than one-million?

def fac(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f

def comb(n,r):
    return int((fac(n)/(fac(r)*fac(n-r))))

br=0
for n in range(1,101):
    for r in range(1,n):
        if comb(n,r)>=1000000:
            br=br+1

print(br)