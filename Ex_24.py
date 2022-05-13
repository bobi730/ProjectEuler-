# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
# If all of the permutations are listed numerically or alphabetically, we call it lexicographic order.
# The lexicographic permutations of 0, 1 and 2 are:
#
# 012   021   102   120   201   210
#
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

def factorial(num):
    if num==0:
        return 1
    return num*factorial(num-1)

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
digits=sorted(digits)
number= 1000000

def nthPerm(number,digits):
    res = ''
    if number>factorial(len(digits)):
        return False
    else:
        current=0
        end=len(digits) - 1
        for pos in range(0,end):
            i=0
            while current<number:
                i=i+1
                current=current+factorial(end-pos)
            current=current-factorial(end-pos)
            res=res+digits[i-1]
            digits.remove(digits[i-1])
        res=res+digits[0]
    return res

print(nthPerm(number,digits))
