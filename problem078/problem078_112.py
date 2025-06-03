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

n = r()
tens=1
nines=1
eights=1
mod = 10**9+7
for i in range(n):
    tens=(tens*10)%mod
    nines=(nines*9)%mod
    eights=(eights*8)%mod
print((tens-2*nines+eights)%mod)