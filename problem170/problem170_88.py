n, k = map(int, input().split())

mod = 10 ** 9 + 7
inv = pow(2, mod - 2) % mod

def calc(b, e, c):
    global mod
    global inv
    res = (e + b) % mod
    res = ((res * c) % mod ) * inv
    return res % mod

ans = 0
for i in range(k, n + 2):
    min_val = calc(0, i - 1, i)
    max_val = calc(n - i + 1, n, i)
    ans += (max_val - min_val + 1) % mod
    ans %= mod

print(ans)