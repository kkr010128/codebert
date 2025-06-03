"""from collections import *
from itertools import *
from bisect import *
from heapq import *

import math
from fractions import gcd"""
import sys
#input = sys.stdin.readline
from heapq import*


N,M=map(int,input().split())
S=list(input())
S.reverse()
idx=0
lst=[]
while idx<N:
    for i in range(1,M+1)[::-1]:
        if i+idx<=N:
            if S[i+idx]=="0":
                idx+=i
                lst.append(i)
                break

    else:
        print(-1)
        exit()
lst.reverse()
print(" ".join([str(i) for i in lst]))
