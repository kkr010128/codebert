import sys
#import numpy as np
import copy

fline = input().rstrip().split(' ')
N, Q = int(fline[0]), int(fline[1])

list = []
for i in range(N):
    tlist = []
    line = input().split(' ')
    tlist = [line[0], line[1]]
    #print(tlist)
    list.append(tlist)

#print(list)
current = 0
while len(list) != 0:
    if int(list[0][1]) <= Q:
        current += int(list[0][1])
        print(list[0][0] + " " + str(current))
        del list[0]
    else:
        list[0][1] = str((int)(list[0][1])-Q)
        list.append(list[0])
        del list[0]
        current += Q
    #print(list)

