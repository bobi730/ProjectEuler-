# In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way....
# The file, poker.txt, contains one-thousand random hands dealt to two players.
# Each line of the file contains ten cards (separated by a single space):
# the first five are Player 1's cards and the last five are Player 2's cards.
# You can assume that all hands are valid (no invalid characters or repeated cards),
# each player's hand is in no specific order, and in each hand there is a clear winner.
#
# How many hands does Player 1 win?

from functools import reduce
file=open('p054_poker.txt')
cards = [x for x in (file.read()).split('\n')]
pOne=[]
pTwo=[]
for hand in cards:
    h=hand.split(' ')
    pOne.append(h[0:5])
    pTwo.append(h[5:])
print(cards)

def value(key):
    fac= {
        "2":2,
        "3":3,
        "4":4,
        "5":5,
        "6":6,
        "7":7,
        "8":8,
        "9":9,
        "T":10,
        "J":11,
        "Q":12,
        "K":13,
        "A":14,
    }
    return fac.get(key,0)

def HighCard(hand):
    val=0
    for card in hand:
            if val<value(card[0]):
                val=value(card[0])
    return val

def Pair(hand):
    val=0
    val2=0
    br=0
    for i in range(0,len(hand)-1):
        for j in range(i+1, len(hand)):
            if hand[i][0]==hand[j][0]:
                if val < value(hand[i][0]):
                    val2=val
                    val = value(hand[i][0])
                else: val2=value(hand[i][0])
    if val!=0:
        br=1
    if val2!=0:
        br=2
    return (br,val,val2)

def TOfAKind(hand):
    bool=False
    val=0
    br=1
    for i in range(0,len(hand)-1):
        for j in range(i+1, len(hand)):
            if hand[i][0]==hand[j][0]:
                br=br+1
        if br==3:
            val = value(hand[i][0])
            bool=True
            return(bool,val)
        br=1
    return (bool,val)

def FOfAKind(hand):
    bool=False
    val=0
    br=1
    for i in range(0,len(hand)-1):
        for j in range(i+1, len(hand)):
            if hand[i][0]==hand[j][0]:
                br=br+1
        if br==4:
            val = value(hand[i][0])
            bool=True
            return(bool,val)
        br=1
    return (bool,val)

def Straight(hand):
    check=[]
    for card in hand:
        check.append(value(card[0]))
    check=sorted(check)
    high=0
    bool=False
    flag=0
    for i in range(0,len(check)-1):
        if check[i]+1==check[i+1]:
            flag=flag+1
    if flag==4:
        bool=True
        high=check[len(check)-1]
    return (bool,high)

def Flush(hand):
    if all([x[-1]==hand[0][1] for x in hand]):
        return HighCard(hand)
    return 0
    #return all(map(lambda c: c[1]==hand[0][1],hand))

def FullHouse(hand):
    if Pair(hand)[2]!=0 and TOfAKind(hand)[0]:
        return TOfAKind(hand)[1]
    return 0

def StraightFlush(hand):
    if Straight(hand)[0] and Flush(hand):
        return HighCard(hand)
    return 0

def RoyalFlush(hand):
    return Straight(hand)[0] and Flush(hand) and Straight(hand)[1]==14

def Score(hand):
    score=str(int(RoyalFlush(hand)))
    score=score+str(StraightFlush(hand))
    score=score+str(FOfAKind(hand)[1])
    score=score+str(FullHouse(hand))
    score=score+str(Flush(hand))
    score=score+str(Straight(hand)[1])
    score=score+str(TOfAKind(hand)[1])
    score=score+str(Pair(hand)[0])
    score=score+str(Pair(hand)[1])
    score=score+str(Pair(hand)[2])
    score=score+str(HighCard(hand))
    return int(score)

wins1=0
for game in range(0,1000):
    if Score(pOne[game])>Score(pTwo[game]):
        wins1=wins1+1
print(wins1)