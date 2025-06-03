MOD = 10**9 + 7


class modint():
    def __init__(self, value):
        self.value = value % MOD

    def __int__(self):
        return int(self.value)

    def __float__(self):
        return float(self.value)

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value)

    def __add__(self, other):
        return (modint(self.value + other.value) if isinstance(other, modint)
                else modint(self.value + other))

    def __sub__(self, other):
        return (modint(self.value - other.value) if isinstance(other, modint)
                else modint(self.value - other))

    def __mul__(self, other):
        return (modint(self.value * other.value) if isinstance(other, modint)
                else modint(self.value * other))

    def __truediv__(self, other):
        return (modint(self.value * pow(other.value, MOD - 2, MOD))
                if isinstance(other, modint)
                else modint(self.value * pow(other, MOD - 2, MOD)))

    def __pow__(self, other):
        return (modint(pow(self.value, other.value, MOD))
                if isinstance(other, modint)
                else modint(pow(self.value, other, MOD)))

    def __eq__(self, other):
        return (self.value == other.value if isinstance(other, modint)
                else self.value == (other % MOD))

    def __ne__(self, other):
        return (self.value == other.value if isinstance(other, modint)
                else self.value == (other % MOD))

    def __radd__(self, other):
        return (modint(other.value + self.value) if isinstance(other, modint)
                else modint(other + self.value))

    def __rsub__(self, other):
        return (modint(other.value - self.value) if isinstance(other, modint)
                else modint(other - self.value))

    def __rmul__(self, other):
        return (modint(other.value * self.value) if isinstance(other, modint)
                else modint(other * self.value))

    def __rtruediv__(self, other):
        return (modint(other.value * pow(self.value, MOD - 2, MOD))
                if isinstance(other, modint)
                else modint(other * pow(self.value, MOD - 2, MOD)))

    def __rpow__(self, other):
        return (modint(pow(other.value, self.value, MOD))
                if isinstance(other, modint)
                else modint(pow(other, self.value, MOD)))

    def modinv(self):
        return modint(pow(self.value, MOD - 2, MOD))


def main():
    import sys
    input = sys.stdin.buffer.readline
    N = int(input())
    A = [int(i) for i in input().split()]

    def gcd(x, y):
        if y == 0:
            return x
        while y != 0:
            x, y = y, x % y
        return x

    def lcm(x, y):
        return x*y//gcd(x, y)

    num = 1
    for a in A:
        num = lcm(num, a)
    n = modint(num)

    ans = 0
    for i, a in enumerate(A):
        ans += n/a
    print(ans)


if __name__ == '__main__':
    main()
