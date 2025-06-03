from sys import stdin
from collections import defaultdict 
# from bisect import *
# from heapq import *
# import math
# mod = 10**9+7

N = input()
A = list(map(int, input().split()))
M = 10**6+1
spf = [i for i in range(M)]
for i in range(2, M):
    if spf[i] == i:
        for j in range(i+i, M, i):
            spf[j] = i
cnt = defaultdict(int)
for a in A:
    ps = set()
    while a != 1:
        ps.add(spf[a])
        a = a // spf[a]
    for p in ps:
        cnt[p] += 1
if all([x < 2 for x in cnt.values()]):
    print("pairwise coprime")
    exit()
gcd = lambda x, y : x if y == 0 else gcd(y, x % y)
x = A[0]
for a in A[1:]:
    x = gcd(x, a)
if x == 1:
    print("setwise coprime")
else:
    print("not coprime")