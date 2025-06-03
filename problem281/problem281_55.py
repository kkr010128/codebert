def main():
    MOD = 10 ** 9 + 7

    X, Y = map(int, input().split())

    if (X + Y) % 3:
        print(0)
        return

    a = (X * 2 - Y) // 3
    b = X - a * 2

    def choose(n, a, mod):
        x, y = 1, 1
        for i in range(a):
            x = x * (n - i) % mod
            y = y * (i + 1) % mod
        return x * pow(y, mod - 2, mod) % mod

    if a < 0 or b < 0:
        print(0)
        return

    ans = choose(a + b, min(a, b), mod=MOD)
    print(ans)


if __name__ == '__main__':
    main()
