#What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

fib=[1,1]
while len(str(fib[len(fib)-1]))<1000:
    current=fib[len(fib)-1]+fib[len(fib)-2]
    fib.append(current)
print(len(fib))