def ncr(n, r):
    num, den = 1, 1
    if n - r < r:
        r = n - r
    for i in range(1, r + 1):
        num *= n - i + 1
        num %= MOD
        den *= i
        den %= MOD
    return num * pow(den, MOD - 2, MOD) % MOD


MOD = 10 ** 9 + 7
X, Y = map(int, input().split())
Z = X + Y

if Z % 3 or Y > 2 * X or Y < X // 2:
    print(0)
else:
    print(ncr(Z // 3, X - Z // 3))

