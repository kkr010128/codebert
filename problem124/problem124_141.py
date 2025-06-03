n_ = 2 * 10**6 + 5
mod = 10**9 + 7
fun = [1] * (n_ + 1)
for i in range(1, n_ + 1):
    fun[i] = fun[i - 1] * i % mod
rev = [1] * (n_ + 1)
rev[n_] = pow(fun[n_], mod - 2, mod)
for i in range(n_ - 1, 0, -1):
    rev[i] = rev[i + 1] * (i + 1) % mod


def nCr(n, r):
    if r > n:
        return 0
    return fun[n] * rev[r] % mod * rev[n - r] % mod


def modinv(x, mod):
    a, b = x, mod
    u, v = 1, 0
    while b:
        t = a // b
        a -= t * b
        a, b = b, a
        u -= t * v
        u, v = v, u
    return u % mod


inv26 = modinv(26, mod)

K = int(input())
S = input()
M = len(S)

ans = 0
po = 1
poo = pow(26, K, mod)
for i in range(K+1):
    ans = (ans + po * poo % mod * nCr(i+M-1, i)) % mod
    po = po * 25 % mod
    poo = poo * inv26 % mod
print(ans)
