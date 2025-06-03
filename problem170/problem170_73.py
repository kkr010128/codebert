import itertools

N, K = map(int, input().split())

N_acum = list(itertools.accumulate(range(N+1)))
mod = 10**9+7
ans = 0
for i in range(K, N+1):
    ans += (N_acum[-1] - N_acum[-(i+1)]) - N_acum[i-1] + 1
    ans %= mod

ans = (ans+1)%mod

print(ans)