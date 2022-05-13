# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
#
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
#
# (Please note that the palindromic number, in either base, may not include leading zeros.)

def palindrome(n):
    if str(n)==str(n)[::-1]:
        return True
    return False
sum=0
for num in range (1,1000000):
    if palindrome(num) and palindrome(str(bin(num))[2:]):
        sum=sum+num
print(sum)