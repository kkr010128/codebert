import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N, K = mapint()
As = sorted(list(mapint()))
Fs = sorted(list(mapint()))[::-1]
from math import ceil

L, R = -1, 10**12
while L+1<R:
    half = (L+R)//2
    k = 0
    for a, f in zip(As, Fs):
        k += max(0, ceil(((a*f)-half)/f))
        if k>K:
            L = half
            break
    else:
        R = half

print(R)