n, k = map(int, input().split())

mod = 1000000007

def pow(x, n):
    ret = 1
    while n > 0:
        if (n & 1) == 1:
            ret = (ret * x) % mod
        x = (x * x) % mod
        n //= 2
    return ret

fac = [1]
inv = [1]
for i in range(n * 2):
    fac.append(fac[-1] * (i + 1) % mod)
    inv.append(pow(fac[-1], mod - 2))

def cmb(n, k):
    if k < 0 or k > n:
        return 0
    return (fac[n] * inv[k] * inv[n - k]) % mod

x = max(0, n - k - 1)
ret = cmb(n * 2 - 1, n - 1)
for i in range(x):
    ret = (ret - cmb(n, i + 1) * cmb(n - 1, i)) % mod
print(ret)

