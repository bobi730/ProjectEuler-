# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example,
# the 5-digit number, 15234, is 1 through 5 pandigital.
#
# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is
# 1 through 9 pandigital.
#
# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
#
# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

perm = []
def permutations(head, tail=''):
    if len(head) == 0:
       perm.append(tail)
    else:
        for i in range(len(head)):
            permutations(head[:i] + head[i+1:], tail + head[i])
permutations('123456789')

panPr=[]
for i in range(0,len(perm)-1):
    if int(perm[i][0])*int(perm[i][1:5])==int(perm[i][5:]):
        panPr.append(int(perm[i][5:]))
    if int(perm[i][:2])*int(perm[i][2:5])==int(perm[i][5:]):
        panPr.append(int(perm[i][5:]))
print(sum(set(panPr)))