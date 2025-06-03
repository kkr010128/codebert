from itertools import chain
N, T = map(int, input().split())
# A = [0]*(N+1)
# B = [0]*(N+1)
AB = [(0, 0)]
for i in range(1, N+1):
    a, b = map(int, input().split())
    # A[i] = a
    # B[i] = b
    AB.append((a, b))
AB.sort()
dp = [[-1]*(6000+1) for _ in range(N+1)]
#dp[i][t]: 注文後にt秒になっている時、i番目までを考慮したとき、
#の最大
dp[0][0] = 0
for i in range(1, N+1):
    a, b = AB[i]
    for t in range(T):
        dp[i][t+a] = max(dp[i][t+a], dp[i-1][t] + b)
        dp[i][t] = max(dp[i][t], dp[i-1][t])
print(max(chain.from_iterable(dp)))