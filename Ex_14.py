#The following iterative sequence is defined for the set of positive integers:
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
# Using the rule above and starting with 13, we generate the following sequence:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
# lthough it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
# Which starting number, under one million, produces the longest chain?

def collatz(start):
    new=start
    br=1
    while new !=1:
        if new%2==0:
            new=new/2
        else:
            new=new*3 +1
        br=br+1
    return(br)
top=0
num=0
for i in range(1,999999):
    current=collatz(i)
    if top<current:
        top=current
        num=i
print(num)