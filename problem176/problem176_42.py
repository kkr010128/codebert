from collections import defaultdict
mod = 10**9 + 7
n, k = map(int, input().split())
l = defaultdict(int)
for i in reversed(range(1, k+1)):
    l[i] = pow(k//i, n, mod)
    a = 2
    while a*i<=k:
        l[i] -= l[a*i]
        l[i] %= mod
        a += 1
ans = 0
for j in l:
    ans += j*l[j] % mod
    ans %= mod
print(ans)