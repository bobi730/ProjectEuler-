#If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

import math
def stotici(key):
    sto= {
        0:0,
        1:10,
        2:10,
        3:12,
        4:11,
        5:11,
        6:10,
        7:12,
        8:12,
        9:11,
    }
    return sto.get(key,'default')
def desetici(key):
    deset= {
        0:0,
        1:0,
        2:6,
        3:6,
        4:5,
        5:5,
        6:5,
        7:7,
        8:6,
        9:6,
    }
    return deset.get(key,'default')
def edinici(key):
    edno= {
        0:0,
        1:3,
        2:3,
        3:5,
        4:4,
        5:4,
        6:3,
        7:5,
        8:5,
        9:4,
    }
    return edno.get(key,'default')
def teen(key):
    naiset= {
        10:3,
        11:6,
        12:6,
        13:8,
        14:8,
        15:7,
        16:7,
        17:9,
        18:8,
        19:8,
    }
    return naiset.get(key,0)

def howMany(num):
    letters=0
    s=str(num)
    if len(s)==1:
        s=(0,0,s[0])
    if len(s)==2:
        s=(0,s[0],s[1])

    if int(s[1])==1:
        letters=stotici(math.floor(num/100))+teen(num%100)
    else:
        letters = stotici(math.floor(num/100)) + desetici(math.floor((num%100)/10)) + edinici(num%10)
    return letters

sum=0
for i in range(0,1000):
    sum=sum+howMany(i)
    if math.floor(i/100)!=0 and i%100!=0:
        sum=sum+3

print(sum+11)