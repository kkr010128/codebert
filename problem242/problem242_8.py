#comb_mod(n, r, mod) = nCr % mod
def comb_mod(n, r, mod):
    ans = 1
    if r <= n/2:
        for i in range(n-r+1, n+1):
            ans *= i
            ans %= mod
        for i in range(1, r+1):
            ans *= pow(i, mod-2, mod)
            ans %= mod
    else:
        for i in range(r+1, n+1):
            ans *= i
            ans %= mod
        for i in range(1, n-r+1):
            ans *= pow(i, mod-2, mod)
            ans %= mod
    return ans

n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

ans = 0
pattern = comb_mod(n-1, k-1, 10**9+7)
for i in range(n-k+1):
    ans += (a[-(i+1)] - a[i]) * pattern
    pattern *= (n-k-i) * pow(n-1-i, 10**9+5, 10**9+7)
    pattern %= 10**9 + 7
print(ans % (10**9+7))