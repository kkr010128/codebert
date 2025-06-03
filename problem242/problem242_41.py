#151_E
n, k = map(int, input().split())
a = sorted(list(map(int, input().split())))
mod = 10 ** 9 + 7

f = [1 for _ in range(n)]
f_inv = [1 for _ in range(n)]
for i in range(2, n):
    f[i] = (f[i-1] * i) % mod
    f_inv[i] = pow(f[i], mod-2, mod)
def comb(n,k):
    return f[n]*f_inv[k]*f_inv[n-k]%mod   
ans = 0
for i in range(n-k+1):
    ans = (ans + comb(n-i-1, k-1) * (a[-i-1]-a[i]))%mod
print(ans)