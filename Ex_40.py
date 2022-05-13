#An irrational decimal fraction is created by concatenating the positive integers:
# 0.123456789101112131415161718192021...
#
# It can be seen that the 12th digit of the fractional part is 1.
#
# If dn represents the nth digit of the fractional part, find the value of the following expression.
#
# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

num=""
for i in range (0,1000077):
    num=num+str(i)
print(int(num[1])*int(num[10])*int(num[100])*int(num[1000])*int(num[10000])*int(num[100000])*int(num[1000000]))