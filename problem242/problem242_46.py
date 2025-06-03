MOD = 10 ** 9 + 7


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


N, K = [int(_) for _ in input().split()]
modf = ModFactorial(N)

A = [int(_) for _ in input().split()]
A.sort()
i = 1
maxv = 0
for i in range(N):
    if K - 1 <= i:
        maxv += modf.nCm(i, K - 1) * A[i]
        maxv %= MOD
# print(maxv)
A.reverse()
minv=0
for i in range(N):
    if K - 1 <= i:
        minv += modf.nCm(i, K - 1) * A[i]
        minv %= MOD
print((maxv-minv)%MOD)
