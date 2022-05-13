# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.

sum=0
prevO=1
prevT=2
fib=0
while fib<=4000000:
    fib=prevO+prevT
    prevO=prevT
    prevT=fib
    if fib%2==0 and fib<=4000000:
        sum+=fib
print(sum+2)