#!/usr/bin/env python3

#import
import math
#import numpy as np
N = int(input())
L = list(map(int, input().split()))

L.sort()

def is_ok(arg, cmin, cmax):
    return L[arg] > cmin and L[arg] < cmax

def meguru_bisect(ok, ng, cmin, cmax):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid, cmin, cmax):
            ok = mid
        else:
            ng = mid
    return ok

ans = 0

for i in range(N - 2):
    for j in range(i + 1, N - 1):
        a = L[i]
        b = L[j]
        cmin = b - a
        cmax = a + b
        t = meguru_bisect(j, N, cmin, cmax)
        ans += t - j

print(ans)