n, k = map(int, input().split())
ps = []
MOD = 998244353
s = set()
for _ in range(k):
    l,r = map(int, input().split())
    ps.append([l,r])

dp = [0] * (n+1)
dp[0] = 1
acc = [0,1]

for i in range(1,n):
    for l, r in ps:
        dp[i] += acc[max(0,i-l+1)] - acc[max(0,i-r)]
    acc.append((acc[i] + dp[i])%MOD)
print(dp[n-1]%MOD)
