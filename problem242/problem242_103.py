import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10 ** 7)

from bisect import bisect_left


def comb(n, k):
    if n < 0 or n < k or k < 0:
        return 0
    return fac[n] * ifac[k] * ifac[n - k] % mod


n, k, *a = map(int, read().split())
a.sort()
mod = 10 ** 9 + 7
max_n = 2 * 10 ** 5 + 1
ans = 0
fac = [1] * max_n
inv = [1] * max_n
ifac = [1] * max_n
for i in range(2, max_n):
    fac[i] = fac[i - 1] * i % mod
    inv[i] = mod - inv[mod % i] * (mod // i) % mod
    ifac[i] = ifac[i - 1] * inv[i] % mod
for i, aa in enumerate(a):
    ans += aa * (comb(i, k - 1) - comb(n - 1 - i, k - 1))
    ans %= mod
print(ans)
