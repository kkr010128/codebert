from math import floor,ceil,sqrt,factorial,log
from collections import Counter, deque
from functools import reduce
import numpy as np
import itertools
def S(): return input()
def I(): return int(input())
def MS(): return map(str,input().split())
def MI(): return map(int,input().split())
def FLI(): return [int(i) for i in input().split()]
def LS(): return list(MS())
def LI(): return list(MI())
def LLS(): return [list(map(str, l.split() )) for l in input()]
def LLI(): return [list(map(int, l.split() )) for l in input()]
def LLSN(n: int): return [LS() for _ in range(n)]
def LLIN(n: int): return [LI() for _ in range(n)]

N = I()

ans = [0 for _ in range(10050)]

for i in range(1,100):
    for j in range(1,100):
        for k in range(1,100):
           v = (i+j+k)**2 - (i*j + j*k + k*i)
           if v < 10050:
            ans[v] += 1

for i in range(N):
    print(ans[i+1])
