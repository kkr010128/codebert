import sys, math
from itertools import permutations, combinations, accumulate
from collections import defaultdict, Counter, deque
from math import factorial#, gcd
from bisect import bisect_left #bisect_left(list, value)
sys.setrecursionlimit(10**7)
enu = enumerate
MOD = 10**9+7
def input(): return sys.stdin.readline()[:-1]
def pri(x): print('\n'.join(map(str, x)))

N = int(input())
G = [list(map(int, input().split())) for _ in range(N)]
c = [0]*N # 0:not found, 1:found, 2:finished
res = [[0]*2 for _ in range(N)]

time = 1
def dfs(index):
#    print('index:', index)
    global time
    if c[index]==0:
        c[index]=1
        res[index][0] = time # found
        time += 1
    elif c[index]==1:
        return
    elif c[index]==2:
        return

    u, k, *v = G[index]
    for node in v:
        dfs(node-1) # 1-index -> 0-index

    c[index] = 2
    res[index][1] = time # finished
    time += 1
    return

for i in range(N):
    dfs(i)
res = [[val1]+val2 for val1, val2 in zip(list(range(1, N+1)), res)]
for val in res:
    print(*val)

