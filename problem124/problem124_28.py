from numba import njit, i8, void
import numpy as np


mod = 10**9+7
k = int(input())
n = len(input())


@njit(i8(i8), cache=True)
def pow(n):
    l, now, mod, k = np.ones(64, np.int64), 1, 10**9+7, 10**9+5
    l[0] = n
    for i in range(1, 64):
        l[i] = l[i-1]*l[i-1] % mod
    for i in range(64):
        if k & 1:
            now = now*l[i] % mod
        k >>= 1
    return now


@njit(void(i8, i8), cache=True)
def num_calc(n, k):
    fact, mod = np.ones(n+k+1, dtype=np.int64), 10**9+7
    for i in range(2, n+k+1):
        fact[i] = fact[i-1]*i % mod

    power = np.ones(k+1, dtype=np.int64)
    power[0] = fact[n+k]
    for i in range(1, k+1):
        power[i] = power[i-1]*25 % mod

    fact = fact[n+k:n-1:-1]*fact[:k+1] % mod
    ans = 0
    for i in range(k+1):
        ans = (ans+pow(fact[i])*power[i]) % mod
    print(ans)


num_calc(n, k)
