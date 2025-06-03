from itertools import accumulate

N, K = map(int, input().split())
mod = 998244353
Move = [list(map(int, input().split())) for _ in range(K)]

DP = [0] * N
DP[0] = 1
DP[1] = -1
cnt = 0

for i in range(N):
    DP[i] += cnt
    DP[i] %= mod
    cnt = DP[i]
    for l, r in Move:
        if i + l < N:
            DP[i+l] += DP[i]
        if i + r + 1 < N:
            DP[i + r + 1] -= DP[i]

print(DP[-1])