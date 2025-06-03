N,K = map(int,input().split())
MOD = 10**9+7
ans = 0
for k in range(K,N+2):
    mx = (N+N-k+1)*k // 2
    mn = (k-1)*k // 2
    ans += mx - mn + 1
    ans %= MOD
print(ans)