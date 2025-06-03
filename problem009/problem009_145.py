import sys, math
from itertools import permutations, combinations
from collections import defaultdict, Counter, deque
from math import factorial#, gcd
from bisect import bisect_left #bisect_left(list, value)
sys.setrecursionlimit(10**7)
enu = enumerate
MOD = 10**9+7
def input(): return sys.stdin.readline()[:-1]
def pri(x): print('\n'.join(map(str, x)))

N = int(input())
ukv = [list(map(int, input().split())) for _ in range(N)]
dist = [-1]*N
dist[0] = 0

deq = deque()
#deq.append(ukv[0][2:])
deq.append([1])

step = 0
while deq[0]:
#    print('deq:', deq)
    nextvs = []
    currvs = deq.popleft()
    for v in currvs:
        for nv in ukv[v-1][2:]:
            if dist[nv-1] == -1:
                dist[nv-1] = step+1
                nextvs.append(nv)
    deq.append(nextvs)
    step += 1

res = [[val1, val2] for val1, val2 in zip(range(1, N+1), dist)]
for a in res:
    print(*a)






