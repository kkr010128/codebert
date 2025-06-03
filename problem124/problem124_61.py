mod = 10 ** 9 + 7

class ModComb:
    def __init__(self, MAX, mod=10 ** 9 + 7):
        fac = [1, 1]
        finv = [1, 1]
        inv = [0, 1]
        for i in range(2, MAX):
            fac.append(fac[i - 1] * i % mod)
            inv.append(mod - inv[mod % i] * (mod // i) % mod)
            finv.append(finv[i - 1] * inv[i] % mod)
        self.fac, self.finv, self.mod = fac, finv, mod

    def nCk(self, n, k):
        if n < k or n < 0 or k < 0:
            return 0
        fac, finv, mod = self.fac, self.finv, self.mod
        return fac[n] * (finv[k] * finv[n - k] % mod) % mod

K = int(input())
S = input()

N = len(S)
mc = ModComb(N + K + 10)

ans = 0
for i in range(K + 1):
    ans += pow(25, i, mod) * pow(26, K - i, mod) * mc.nCk(i + N - 1, N - 1)
    ans %= mod

print(ans)