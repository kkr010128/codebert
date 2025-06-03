#!/usr/bin/env python3

N, K, S = map(int, input().split())
if S < 10**9:
    Ret = [S]*K + [S+1]* (N-K)
else:
    Ret = [S]*K + [1]* (N-K)
print(*Ret)
