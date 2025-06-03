N, K = list(map(int, input().split()))
C = 998244353
L = [None]*K
for j in range(K):
    l, r = list(map(int, input().split()))
    L[j] = [l, r+1]

dp = [0]*N
dp[0] = 1
imos = [0]*(N+1)
imsm = [0]*N

for i in range(N-1):
    if i > 0:
        imsm[i] = imsm[i-1]+imos[i]
        dp[i] = imsm[i] % C
    a = dp[i]
    # print(i,dp)
    for j in range(K):
        l, r = L[j]
        nl = min(i+l, N)
        nr = min(i+r, N)
        imos[nl] += a
        imos[nr] -= a
        # print(i, imos)
dp[N-1] = (imsm[N-2]+imos[N-1]) % C
print(dp[N-1])
