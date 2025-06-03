import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)
from collections import defaultdict
from bisect import *
mod = 10**9+7

N = int(input())
A = list(map(int, input().split()))
cnt = [0]*3
ans = 1
for i, x in enumerate(A):
    T = len([c for c in cnt if c == x])
    for i, c in enumerate(cnt):
        if c == x:
            cnt[i] += 1
            break
    ans = ans * T % mod
print(ans)
