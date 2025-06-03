N, K = [int(_) for _ in input().split()]
MOD = 10 ** 9 + 7

ans = 0


class ModFactorial:
    """
    階乗, 組み合わせ, 順列の計算
    """

    def __init__(self, n, MOD=10 ** 9 + 7):
        """

        :param n: 最大の要素数.
        :param MOD:
        """
        kaijo = [0] * (n + 10)
        gyaku = [0] * (n + 10)

        kaijo[0] = 1
        kaijo[1] = 1
        for i in range(2, len(kaijo)):
            kaijo[i] = (i * kaijo[i - 1]) % MOD
        gyaku[0] = 1
        gyaku[1] = 1
        for i in range(2, len(gyaku)):
            gyaku[i] = pow(kaijo[i], MOD - 2, MOD)
        self.kaijo = kaijo
        self.gyaku = gyaku
        self.MOD = MOD

    def nCm(self, n, m):
        return (self.kaijo[n] * self.gyaku[n - m] * self.gyaku[m]) % self.MOD

    def nPm(self, n, m):
        return (self.kaijo[n] * self.gyaku[n - m]) % self.MOD

    def factorial(self, n):
        return self.kaijo[n]


mf = ModFactorial(N, MOD)
for i in range(1, N + 1):
    if N - i > K: continue

    p = N - i
    # print(i, p, mf.nCm(p + i - 1, i - 1))
    ans += mf.nCm(p + i - 1, i - 1) * mf.nCm(N, i)
    ans %= MOD
print(ans)
