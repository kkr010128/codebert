def factorial(n, mod):
    fac = [0] * (n + 1)
    inv = [0] * (n + 1)
    fac[0], inv[0] = 1, 1
    for i in range(1, n + 1):
        fac[i] = fac[i-1] * i % mod
        inv[i] = inverse(fac[i], mod)
    return fac, inv

def inverse(a, mod):
    a %= mod # 除数が正なら正になる
    p = mod
    x, y = 0, 1
    while a > 0:
        n = p // a
        p, a = a, p % a, 
        x, y = y, x - n * y
    return x % mod # 除数が正なら正になる

mod = 10 ** 9 + 7
n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
fac, inv = factorial(n, mod)

ans = 0
for i in range(0, n-k+1):
    m = n - i - 1
    ans = (ans + (a[-i-1] - a[i]) % mod * fac[m] % mod * inv[m-k+1] % mod * inv[k-1]) % mod
print(ans)

