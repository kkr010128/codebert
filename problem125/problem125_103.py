import sys 
import collections

X = int(input())

Angle = 360
for i in range(1,10**9):

    if Angle < (X*i):
        Angle = Angle + 360 

    if (Angle / (X*i)) == 1:
        print(i)
        sys.exit()