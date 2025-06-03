import sys
import numpy as np

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    X, Y = map(int, readline().split())
    if X%3==Y%3==1 or X%3==Y%3==2:
        print(0)
        sys.exit()
    a = (2*Y-X)//3
    b = (2*X-Y)//3


    N = a+b
    fact = [1, 1]
    factinv = [1, 1]
    inv = [0, 1]

    for i in range(2, N + 1):
        fact.append((fact[-1] * i) % MOD)
        inv.append((-inv[MOD % i] * (MOD // i)) % MOD)
        factinv.append((factinv[-1] * inv[-1]) % MOD)

    def cmb(n, r, mod):
        if (r < 0) or (n < r):
            return 0
        r = min(r, n - r)
        return fact[n] * factinv[r] * factinv[n - r] % mod

    print(cmb(N, a, MOD))


if __name__ == '__main__':
    main()
