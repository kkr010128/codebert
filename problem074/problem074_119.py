N,K = map(int,input().split())

MOD = 998244353

interval = []
for i in range(K):
    intv = [int(x) for x in input().split()]
    interval.append(intv)

dp = [0]*N
diff = [0]*(N-1)
dp[0] = 1
diff[0] = -1

for i in range(N-1):
    for L,R in interval:
        if L <= N-1 - i:
            diff[i+L-1] += dp[i]
        if R+1 <= N-1 - i:
            diff[i+R] -= dp[i]
    dp[i+1] = dp[i] + diff[i]
    dp[i+1] %= MOD

print(dp[N-1])