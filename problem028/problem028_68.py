#!/usr/bin/env python
from math import *
n, m = list(map(int, input().split()))
c = list(map(int, input().split()))
DP = [n for i in range(n + 1)]
DP[0] = 0
for cost in c:
	for i in range(cost, n + 1):
		DP[i] = min(DP[i], DP[i - cost] + 1)
print(DP[n])

