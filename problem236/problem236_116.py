import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)
from collections import defaultdict
from bisect import *
mod = 10**9+7

H = int(input())
W = int(input())
N = int(input())
h, w = max(H, W), min(H, W)
cnt, ans = 0, 0
while cnt < N:
    cnt += h
    ans += 1
print(ans)
