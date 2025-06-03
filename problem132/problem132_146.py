N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

dp = [0] * (N + 1)
for k in range(K):
    sta = [max(i-A[i], 0) for i in range(N)]
    end = [min(i+A[i]+1, N) for i in range(N)]
    for s in sta:
        dp[s] += 1
    for e in end:
        dp[e] -= 1
    for i in range(1, len(dp)-1):
        dp[i] += dp[i-1]
    B = dp[:-1]
    if A == B:
        break
    A = B
    dp = [0] * (N + 1)
 
print(' '.join(map(str, A)))