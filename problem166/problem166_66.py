#import numpy as np
import sys, math
from itertools import permutations, combinations
from collections import defaultdict, Counter, deque
from math import factorial#, gcd
from bisect import bisect_left, bisect_right #bisect_left(list, value)
sys.setrecursionlimit(10**7)
enu = enumerate
MOD = 2019
def input(): return sys.stdin.readline()[:-1]
pl = lambda x: print(*x, sep='\n')

S = input()
N = len(S)

d = defaultdict(int)
d[0] += 1
# nums = [0]*(N+1)
m = 0
last = 0
dd = 1
for i in range(N):
    m += int(S[N-i-1])*dd
    m %= MOD
    # val = (int(S[i])*m + nums[i])%MOD
    # cnt += d[val]
    dd = (dd*10)%MOD
    d[m] += 1

cnt = 0
for i, v in d.items():
    cnt += v*(v-1)//2
print(cnt)