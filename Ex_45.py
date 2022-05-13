# Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:
#
# Triangle	 	Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
# Pentagonal	 	Pn=n(3n−1)/2	 	1, 5, 12, 22, 35, ...
# Hexagonal	 	Hn=n(2n−1)	 	1, 6, 15, 28, 45, ...
# It can be verified that T285 = P165 = H143 = 40755.
#
# Find the next triangle number that is also pentagonal and hexagonal.

def isTriangle(num):
    test= (-1+(1+8*num)**(1/2))/2;
    if test%1==0:
        return True
    return False

def isPentagonal(num):
    test= (1+(1+24*num)**(1/2))/6;
    if test%1==0:
        return True
    return False

def isHexagonal(num):
    test= (1+(1+8*num)**(1/2))/4;
    if test%1==0:
        return True
    return False

i=286
flag=False
while flag==False:
    num=i*(i+1)/2
    if isPentagonal(num) and isHexagonal(num):
        flag=True
        print(num)
    i=i+1