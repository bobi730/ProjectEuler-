# It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.
#
# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

test=1
flag=False
while flag==False:
    two=sorted(set(list(str(2*test))))
    three=sorted(set(list(str(3*test))))
    four=sorted(set(list(str(4*test))))
    five=sorted(set(list(str(5*test))))
    six=sorted(set(list(str(6*test))))
    if two==three and three==four and four==five and five==six:
        print(test)
        flag=True
    test=test+1