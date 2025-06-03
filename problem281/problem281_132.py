MOD = 10**9 + 7
X, Y = map(int, input().split())


def f(n):
    res = n
    for i in range(1, n):
        res *= i
        res %= MOD
    return res


def solve():
    ans = 0
    if (X + Y) % 3 == 0:
        n = (2 * X - Y) // 3
        m = (2 * Y - X) // 3
        if n == 0 or m == 0:
            ans += 1
        elif n > 0 and m > 0:
            ans += (f(n + m) * pow(f(n), MOD - 2, MOD) * pow(f(m), MOD - 2, MOD)) % MOD

    print(ans)


if __name__ == "__main__":
    solve()