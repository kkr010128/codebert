import sys
from collections import defaultdict, Counter

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def prime_factorize(n):
    a = Counter()
    while n % 2 == 0:
        a[2] += 1
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a[f] += 1
            n //= f
        else:
            f += 2
    if n != 1:
        a[n] += 1
    return a


def main():
    N, *A = map(int, read().split())

    lcm_prime = Counter()
    for a in A:
        for p, n in prime_factorize(a).items():
            if lcm_prime[p] < n:
                lcm_prime[p] = n

    l = 1
    for p, n in lcm_prime.items():
        l = l * pow(p, n, MOD) % MOD

    ans = 0
    for a in A:
        ans = (ans + pow(a, MOD - 2, MOD)) % MOD

    ans = ans * l % MOD

    print(ans)
    return


if __name__ == '__main__':
    main()
