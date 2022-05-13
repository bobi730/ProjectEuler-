#Find the sum of the digits in the number 100!

def factorial(num):
    if num==0:
        return 1
    return num*factorial(num-1)

a=factorial(100)
a=list(map(int,str(a)))
print(sum(a))