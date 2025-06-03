MOD = 1000000007
N, K = map(int, input().split())
ans = 0
f = [0] * (K+1)
g = [0] * (K+1)
for t in range(K, 0, -1):
    f[t] = pow(K//t, N, MOD)
    g[t] = f[t]
    for s in range(2 * t, K+1, t):
        g[t] -= g[s]
    ans = (ans + t * g[t]) % MOD
print(ans)