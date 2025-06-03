import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    n, k = list(map(int, readline().split()))

    comb1 = [0] * (n + 1)
    comb2 = [0] * (n + 1)

    comb1[0] = 1
    comb2[0] = 1

    for i in range(1, n + 1):
        comb1[i] = comb1[i - 1] * (n + 1 - i)
        comb2[i] = comb2[i - 1] * (n - i)
        comb1[i] %= MOD
        comb2[i] %= MOD
        inv = pow(i, MOD - 2, MOD)
        comb1[i] *= inv
        comb2[i] *= inv
        comb1[i] %= MOD
        comb2[i] %= MOD

    r = min(k, n - 1)
    ans = 0
    for i in range(r + 1):
        ans += comb1[n - i] * comb2[n - 1 - i]
        ans %= MOD

    print(ans)


if __name__ == '__main__':
    main()
