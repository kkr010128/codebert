from sys import exit
import copy
#import numpy as np
#from collections import deque


d, = map(int, input().split())
c= list(map(int, input().split()))
s=[list(map(int, input().split())) for _ in range(d)]
#  t=[int(input()) for _ in range(d)]

sche=[0 for _ in range(d)]
last=[0 for _ in range(26)]

score=0
for day in range(1,d+1):
    idx=day-1
    d_tmp=0
    i_tmp=0
    for t in range(26):    
        delta=0
        l_tmp=copy.copy(last)
        delta+=s[idx][t]
        l_tmp[t]=day
        for l in range(26):
            delta-=c[l]*(day-l_tmp[l])
        if delta>=d_tmp:
            d_tmp=delta
            i_tmp=t
    sche[idx]=i_tmp
    score+=d_tmp
    last[i_tmp]=day
    # print(score)
    print(i_tmp+1)



