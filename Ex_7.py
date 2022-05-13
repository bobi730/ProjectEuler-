#What is the 10 001st prime number?

top=1400000
l=list(range(0,top))
primes=[]
def cull(l,num):
    for i in range(num,len(l),num):
        l[i]=0
for i in range(2,len(l)):
    if l[i]!=0:
        primes.append(l[i])
        cull(l,l[i])
print(primes[10000])