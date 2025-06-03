# coding: utf-8
import sys

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

MOD = 10 ** 9 + 7
N, K = lr()
answer = 0
for i in range(K, N+2):
    low = i * (i-1) // 2
    high = i * (N+N-i+1) // 2
    answer += high - low + 1
    answer %= MOD

print(answer%MOD)
