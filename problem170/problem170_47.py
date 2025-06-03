N, K = map(int, input().split())

kMod = 10**9+7

ans = 0

for k in range(K, N+2):
    lb = (k-1) * k // 2
    ub = (N+1-k + N) * k // 2
    ans += (ub-lb+1)
    ans %= kMod
print(ans)