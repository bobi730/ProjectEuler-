
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

sumPow=0
sumSumPow=0
for num in range(1,101):
    sumPow=sumPow+num**2
    sumSumPow=sumSumPow+num
sumSumPow=sumSumPow**2
print(sumSumPow-sumPow)