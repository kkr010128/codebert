import sys
from collections import defaultdict, Counter

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, *A = map(int, read().split())

    N_MAX = 10 ** 6

    min_factor = list(range(1, N_MAX + 1, 2))
    for i in range(1, int((N_MAX ** 0.5 - 1) / 2) + 1):
        f = 2 * i + 1
        if min_factor[i] != f:
            continue
        for j in range(2 * i * (i + 1), len(min_factor), f):
            if min_factor[j] > f:
                min_factor[j] = f

    def prime_factorize_fast(n):
        a = Counter()
        while not n & 1:
            a[2] += 1
            n //= 2
        while n != 1:
            a[min_factor[(n - 1) // 2]] += 1
            n //= min_factor[(n - 1) // 2]

        return a

    lcm_prime = Counter()
    for a in A:
        for p, n in prime_factorize_fast(a).items():
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
