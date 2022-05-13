#What is the sum of the digits of the number 21000?

num=2**1000
num=str(num)
arr=[]
for d in range(0,len(num)):
    arr.append(int(num[d]))
print(sum(arr))