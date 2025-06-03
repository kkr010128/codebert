import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60


def mod_com_once(n, r, MOD):
    if n < r:
        return 0
    if n < 0 or r < 0:
        return 0
    r = min(r, n - r)
    numer = denom = 1
    for i in range(n - r + 1, n + 1):
        numer = numer * i % MOD
    for i in range(1, r + 1):
        denom = denom * i % MOD
    return numer * pow(denom, MOD - 2, MOD) % MOD


def main():
    MOD = 1000000007
    X, Y = map(int, readline().split())

    p = (2 * X - Y) // 3
    q = (-X + 2 * Y) // 3

    if (X + Y) % 3 or p < 0 or q < 0:
        print(0)
        return

    print(mod_com_once(p + q, p, MOD))
    return


if __name__ == '__main__':
    main()
