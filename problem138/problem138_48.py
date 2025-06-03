import sys
from collections import defaultdict
from queue import deque
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10**8)


def geta(fn=lambda s: s.decode()):
    return map(fn, readline().split())


def gete(fn=lambda s: s.decode()):
    return fn(readline().rstrip())


def egcd(a: int, b: int):
    """
    A solution of ax+by=gcd(a,b). Returns
    (gcd(a,b), (x, y)).
    """
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = egcd(b % a, a)
        return g, y - (b // a) * x, x


def modinv(a: int, mod: int = 10**9 + 7):
    """
    Returns a^{-1} modulo m.
    """
    g, x, y = egcd(a, mod)
    if g > 1:
        raise Exception('{}^(-1) mod {} does not exist.'.format(a, mod))
    else:
        return x % mod


import numpy as np


def main():
    N, S = geta(int)
    A = list(geta(int))
    A.sort()
    mod = 998244353

    inv2 = modinv(2, mod)

    dp = np.zeros((N + 1, S + 1), dtype=np.int64)

    _t = pow(2, N, mod)
    dp[:, 0] = _t
    for i in range(1, N + 1):
        dp[i, :] = dp[i - 1, :]
        if A[i - 1] <= S:
            tmp = np.roll(dp[i - 1, :], A[i - 1])
            tmp[:A[i - 1]] = 0
            dp[i, :] += tmp * inv2
            dp[i, :] %= mod

    print(dp[N][S])


if __name__ == "__main__":
    main()