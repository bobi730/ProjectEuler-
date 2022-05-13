#Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
# there are exactly 6 routes to the bottom right corner.

#How many such routes are there through a 20×20 grid?

import numpy
arr = numpy.empty(shape=(21,21),dtype='object')
for i in range(0,21):
    arr[0][i]=1
    arr[i][0]=1
for i in range(1,21):
    for j in range(1,21):
        arr[i][j]=arr[i-1][j]+arr[i][j-1]
print(arr[20][20])