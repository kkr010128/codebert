class FastModComb:

    def __init__(self, n, mod=10 ** 9 + 7):
        f, self.mod = [1], mod
        for i in range(1, n + 1):
            f.append(f[-1] * i % mod)
        rf = [self.modpow(f[-1], mod - 2)]
        for i in range(1, n + 1):
            rf.append(rf[-1] * (n - i + 1) % mod)
        self.f, self.rf = f, list(reversed(rf))

    def modpow(self, a, b):
        ret = 1
        while b > 0:
            if b % 2 == 1:
                ret = ret * a % self.mod
            a = a * a % self.mod
            b //= 2
        return ret

    def modcomb(self, n, c):
        return self.f[n] * self.rf[c] * self.rf[n - c] % self.mod


n, k = map(int, input().split())
mod, mc = 10 ** 9 + 7, FastModComb(n)
print(sum([mc.modcomb(n, m) * mc.modcomb(n - 1, n - m - 1) % mod
           for m in range(min(n - 1, k) + 1)]) % mod)
