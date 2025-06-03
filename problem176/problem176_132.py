class ModInt:
    def __init__(self, x):
        self.x = x % MOD

    def __str__(self):
        return str(self.x)

    __repr__ = __str__

    def __add__(self, other):
        return (
            ModInt(self.x + other.x) if isinstance(other, ModInt) else
            ModInt(self.x + other)
        )

    def __sub__(self, other):
        return (
            ModInt(self.x - other.x) if isinstance(other, ModInt) else
            ModInt(self.x - other)
        )

    def __mul__(self, other):
        return (
            ModInt(self.x * other.x) if isinstance(other, ModInt) else
            ModInt(self.x * other)
        )

    def __truediv__(self, other):
        return (
            ModInt(
                self.x * pow(other.x, MOD - 2, MOD)
            ) if isinstance(other, ModInt) else
            ModInt(self.x * pow(other, MOD - 2, MOD))
        )

    def __pow__(self, other):
        return (
            ModInt(self.power_func(self.x, other.x, MOD)) if isinstance(other, ModInt) else
            ModInt(self.power_func(self.x, other, MOD))
        )

    __radd__ = __add__

    def __rsub__(self, other):
        return (
            ModInt(other.x - self.x) if isinstance(other, ModInt) else
            ModInt(other - self.x)
        )

    __rmul__ = __mul__

    def __rtruediv__(self, other):
        return (
            ModInt(
                other.x * pow(self.x, MOD - 2, MOD)
            ) if isinstance(other, ModInt) else
            ModInt(other * pow(self.x, MOD - 2, MOD))
        )

    def __rpow__(self, other):
        return (
            ModInt(pow(other.x, self.x, MOD)) if isinstance(other, ModInt) else
            ModInt(pow(other, self.x, MOD))
        )

    def power_func(self,a,n,p):
        bi=str(format(n,"b"))#2進表現に
        res=1
        for i in range(len(bi)):
            res=(res*res) %p
            if bi[i]=="1":
                res=(res*a) %p
        return res
#グローバル変数MODを決めてあげてください

#グローバル変数MODを決めてあげてください
MOD = 10**9 + 7

N,K=[int(hoge) for hoge in input().split()]
Kazus = [0]*(K+1)
for x in range(K,0,-1):
    Dmax = K//x
    MoDmax = ModInt(Dmax)
    kazu = MoDmax ** N
    for d in range(Dmax,1,-1):
        kazu -= Kazus[d*x]
    Kazus[x] = kazu

print(sum([x*k for x,k in enumerate(Kazus) ]))
