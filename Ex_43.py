# The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9
# in some order, but it also has a rather interesting sub-string divisibility property.
#
# Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:
#
# d2d3d4=406 is divisible by 2
# d3d4d5=063 is divisible by 3
# d4d5d6=635 is divisible by 5
# d5d6d7=357 is divisible by 7
# d6d7d8=572 is divisible by 11
# d7d8d9=728 is divisible by 13
# d8d9d10=289 is divisible by 17
# Find the sum of all 0 to 9 pandigital numbers with this property.

perm = []
def permutations(head, tail=''):
    if len(head) == 0:
       perm.append(tail)
    else:
        for i in range(len(head)):
            permutations(head[:i] + head[i+1:], tail + head[i])
permutations('0123456789')

permCull=[]
for s in perm:
    if int(s[5])%5==0 and int(s[3])%2==0 and (int(s[2])+int(s[3])+int(s[4]))%3==0:
        permCull.append(s)

def property(string):
    # int(string[1:4]) % 2 == 0 and int(string[2:5]) % 3 == 0 and int(string[3:6]) % 5 == 0 and
    if int(string[4:7])%7==0 and int(string[5:8])%11==0 and int(string[6:9])%13==0 and int(string[7:10])%17==0:
        return True
    return False

sum=0
for st in permCull:
    if property(st)==True:
        sum=sum+int(st)

print(sum)