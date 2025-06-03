N,S,*A = map(int, open(0).read().split())
dp = [[0] * (S+1) for _ in range(N+1)]
dp[0][0] = 1
appeared = set([0])
for i in range(1,N+1):
    temp = A[i-1]
    ts = set()
    for x in appeared:
        dp[i][x] += (dp[i-1][x]*2) % 998244353
        if temp + x <= S:
            dp[i][temp+x] += dp[i-1][x]
            if temp + x not in appeared:
                ts.add(temp+x)
    appeared |= ts
print(dp[N][S]%998244353)