import os
import sys
import math
import heapq
from decimal import *
from io import BytesIO, IOBase
from collections import defaultdict, deque

def r():
    return int(input())
def rm():
    return map(int,input().split())
def rl():
    return list(map(int,input().split()))

n=r()
a=rl()
money=1000
s=0

for i in range(n):
    if i==n-1:
        money+=s*a[i]
    else:
        if a[i]<=a[i+1]:
            money+=s*a[i]
            s=money//a[i]
            money%=a[i]
        else:
            money+=s*a[i]
            s=0
print(money)