# -*- coding: utf-8 -*-
def inpl(): return list(map(int, input().split()))
n, m = inpl()
C = sorted(inpl())
DP = list(range(n+1))

for c in C[1:]:
    for i in range(n-c+1):
        if DP[i] + 1 < DP[i+c]:
            DP[i+c] = DP[i] + 1
            
print(DP[-1])
