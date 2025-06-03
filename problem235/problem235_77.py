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

    min_factor = list(range(N_MAX + 1))
    min_factor[2::2] = [2] * (N_MAX // 2)
    for i in range(3, int(N_MAX ** 0.5) + 2, 2):
        if min_factor[i] != i:
            continue
        for j in range(i * i, N_MAX + 1, 2 * i):
            if min_factor[j] > i:
                min_factor[j] = i

    def prime_factorize_fast(n):
        a = Counter()
        while n != 1:
            a[min_factor[n]] += 1
            n //= min_factor[n]

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
