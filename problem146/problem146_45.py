import bisect
import collections
import functools
import heapq
import math
from collections import deque
from collections import defaultdict
MOD = 10**9+7

N = int(input())
A = [0]*N
B = [0]*N
C = [[0]*2 for _ in range(N)]
zero = 0
no_inf = 0
inf = 0
for i in range(N):
    A[i],B[i] = map(int,(input().split()))
    if A[i] == 0 and B[i] == 0:
        C[i] = (0,0)
        zero += 1
    elif A[i] == 0:
        C[i] = (0,0)
        no_inf += 1
    elif B[i] == 0:
        C[i] = (0,0)
        inf += 1
    elif B[i] > 0:
        g = math.gcd(A[i],B[i])
        C[i] = (A[i]//g,B[i]//g)
    else:
        g = math.gcd(A[i],B[i])
        C[i] = (-A[i]//g,-B[i]//g)

d = defaultdict(int)

for i in range(N):
    if C[i] != (0,0):
        d[C[i]] += 1

ans = 1
for k in d.keys():
    if k[0] > 0:
        if (-k[1],k[0]) in d:
            ans *= pow(2,d[k],MOD) + pow(2,d[(-k[1],k[0])],MOD) -1
            d[k],d[(-k[1],k[0])] = 0,0
        else:
            ans *= pow(2,d[k],MOD)
    else:
        if (k[1],-k[0]) in d:
            ans *= pow(2,d[k],MOD) + pow(2,d[(k[1],-k[0])],MOD) -1
            d[k],d[(k[1],-k[0])] = 0,0
        else:
            ans *= pow(2,d[k],MOD)

ans *= pow(2,no_inf,MOD) + pow(2,inf,MOD) -1
print((ans+zero-1)%MOD)