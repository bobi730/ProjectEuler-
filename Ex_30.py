# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
#
# 1634 = 14 + 64 + 34 + 44
# 8208 = 84 + 24 + 04 + 84
# 9474 = 94 + 44 + 74 + 44
# As 1 = 14 is not a sum it is not included.
#
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
#
# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

total=0
cullSet=[]
for num in range(2,354295):
    strN=str(num)
    fifth=0
    for l in strN:
        fifth=fifth+int(l)**5
    if fifth==num:
        total=total+num
print(total)