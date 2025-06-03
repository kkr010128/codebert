n, k = map(int, input().split())
mod = 10 ** 9 + 7


class ModInt:
    def __init__(self, num, mod):
        self.num = num
        self.mod = mod

    def __str__(self):
        return str(self.num)

    def __repr__(self):
        return "ModInt(num: {}, mod: {}".format(self.num, self.mod)

    def __add__(self, other):
        ret = self.num + other.num
        ret %= self.mod
        return ModInt(ret, self.mod)

    def __sub__(self, other):
        ret = self.num - other.num
        ret %= self.mod
        return ModInt(ret, self.mod)

    def __mul__(self, other):
        ret = self.num * other.num
        ret %= self.mod
        return ModInt(ret, self.mod)

    def pow(self, times):
        pw = pow(self.num, times, self.mod)
        return ModInt(pw, self.mod)

    def inverse(self):
        return self.pow(self.mod - 2)

    def __truediv__(self, other):
        num = self * other.inverse()
        return ModInt(num, self.mod)


class Combination:
    def __init__(self, n, mod):
        self.mod = mod
        self.fact = [ModInt(1, mod)]
        self.inverse = [ModInt(1, mod)]
        for i in range(1, n + 1):
            self.fact.append(self.fact[-1] * ModInt(i, mod))
            self.inverse.append(self.inverse[-1] * ModInt(i, mod).inverse())

    def comb(self, n, k):
        if k < 0 or n < k:
            return ModInt(0, self.mod)

        return self.fact[n] * self.inverse[k] * self.inverse[n-k]


mx = min(k, n - 1)
comb = Combination(n, mod)
ans = ModInt(0, mod)

for i in range(mx + 1):
    ans += comb.comb(n, i) * comb.comb(n - 1, i)

print(ans)
