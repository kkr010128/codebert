import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, K, *A = map(int, read().split())

    COM_MAX = N

    fac, finv, inv = [0] * (COM_MAX + 1), [0] * (COM_MAX + 1), [0] * (COM_MAX + 1)
    fac[0] = fac[1] = finv[0] = finv[1] = inv[1] = 1

    for i in range(2, COM_MAX + 1):
        fac[i] = fac[i - 1] * i % MOD
        inv[i] = MOD - inv[MOD % i] * (MOD // i) % MOD
        finv[i] = finv[i - 1] * inv[i] % MOD

    def com(n, r):
        if n < 0 or r < 0 or n < r:
            return 0
        return fac[n] * (finv[r] * finv[n - r] % MOD) % MOD

    A.sort()

    ans = 0
    for i, a in enumerate(A):
        ans = (ans + a * com(i, K - 1) % MOD) % MOD
        ans = (ans - a * com(N - i - 1, K - 1) % MOD) % MOD

    print(ans)
    return


if __name__ == '__main__':
    main()
