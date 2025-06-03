import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


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
    X, Y = map(int, readline().split())

    if (X + Y) % 3:
        print(0)
        return

    p, q = (-X + 2 * Y) // 3, (2 * X - Y) // 3
    if p < 0 or q < 0:
        print(0)
        return

    ans = mod_com_once(p + q, p, MOD)

    print(ans)
    return


if __name__ == '__main__':
    main()
