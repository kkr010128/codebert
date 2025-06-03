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

mod = 998244353

N, M, K = map(int, input().split())

mc = ModComb(N, mod)

ans = 0
for k in range(K + 1):
    ans += M * pow(M - 1, N - 1 - k, mod) * mc.nCk(N - 1, k)
    ans %= mod

print(ans)