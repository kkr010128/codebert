import sys
import math
import collections

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline


def main():
    K = int(input())
    S = input().strip()

    MOD = 10 ** 9 + 7

    fact = [1, 1]
    factinv = [1, 1]
    inv = [0, 1]

    def cmb(n, k, p):
        if (k < 0) or (n < k):
            return 0
        r = min(k, n - k)
        return fact[n] * factinv[k] * factinv[n - k] % p

    N = 10 ** 6 * 2
    for i in range(2, N + 1):
        fact.append((fact[-1] * i) % MOD)
        inv.append((-inv[MOD % i] * (MOD // i)) % MOD)
        factinv.append((factinv[-1] * inv[-1]) % MOD)

    ans = 0
    a = 1
    b = pow(26, K, MOD)
    for i in range(K + 1):
        ans += a * cmb(i + len(S) - 1, len(S) - 1, MOD) * b
        a = a * 25 % MOD
        b = b * pow(26, MOD - 2, MOD) % MOD

    print(ans % MOD)


if __name__ == '__main__':
    main()
