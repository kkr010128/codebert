#!/usr/bin/env python3

#import
#import math
#import numpy as np
#= int(input())
S = input()
K = int(input())
ls = len(S)
t1 = []

t = 1
for i in range(1, ls):
    if S[i - 1] == S[i]:
        t += 1
    else:
        if t > 1:
            t1.append(t)
        t = 1

if t > 1 or t == ls:
    t1.append(t)

ans = 0
for t in t1:
    ans += t // 2

if len(t1) == 1:
    if t1[0] == ls:
        print(ls * K // 2)

else:
    if S[0] != S[-1]:
        print(ans * K)
    
    else:
        ta = t1[0]
        tb = t1[-1]
        print(ans * K - (ta // 2 + tb // 2 - (ta + tb) // 2) * (K - 1))




