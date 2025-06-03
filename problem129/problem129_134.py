import collections
import heapq
import math
import random
import sys
input = sys.stdin.readline
sys.setrecursionlimit(500005)
ri = lambda: int(input())
rl = lambda: list(map(int, input().split()))
rs = lambda: input().rstrip()

n = ri()
a = rl()
N = 1000000
f = [0] * (N + 10)
for v in a:
    f[v] += 1
for i in range(N, 0, -1):
    if f[i] == 0:
        continue
    j = i * 2
    while j <= N:
        f[j] += f[i]
        j += i
cnt = sum(f[i] == 1 for i in a)
print(cnt)

