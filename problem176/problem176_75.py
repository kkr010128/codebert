N, K = map(int, input().split())
MOD = 10**9+7

c = [0]*(K+1)
for i in range(1, K+1)[::-1]:
    c[i] = pow(K//i, N, MOD)
    for j in range(i*2, K+1, i):
        c[i] -= c[j]
        if c[i]<0:
            c[i] += MOD

ans = 0
for i in range(1, K+1):
    ans += i*c[i]
ans %= MOD

print(ans)