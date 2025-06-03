#!/usr/bin/env python3
from bisect import bisect_right

n, *L = map(int, open(0).read().split())
L.sort()
ans = 0
for i in range(n):
    for j in range(i + 1, n):
        ans += (bisect_right(L, L[i] + L[j] - 1) -
                bisect_right(L, L[j] - L[i]) - 1 - (L[j] - L[i] * 2 < 0))
print(ans // 3)
