N,M = map(int, input().split())
C = list(map(int, input().split()))

C.sort()
DP = [i for i in range(N+1)]

for m in range(1,M):
    coin = C[m]
    for total in range(1, N+1):
        if total - coin >= 0:
            DP[total] = min(DP[total], DP[total - coin] + 1)

print(DP[-1])
