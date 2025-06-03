
MOD = 998244353
class mint:
    def __init__(self, x):
        if isinstance(x, int):
            self.x = x % MOD 
        elif isinstance(x, mint):
            self.x = x.x
        else:
            self.x = int(x) % MOD 
    def __str__(self):
        return str(self.x)
    __repr__ = __str__
    def __iadd__(self, other):
        self.x += other.x if isinstance(other, mint) else other
        self.x -= MOD if self.x >= MOD else 0
        return self
    def __isub__(self, other):
        self.x += MOD-other.x if isinstance(other, mint) else MOD-other
        self.x -= MOD if self.x >= MOD else 0
        return self
    def __imul__(self, other):
        self.x *= other.x if isinstance(other, mint) else other
        self.x %= MOD
        return self
    def __add__(self, other):
        return (
            mint(self.x + other.x) if isinstance(other, mint) else
            mint(self.x + other)
        )
    def __sub__(self, other):
        return (
            mint(self.x - other.x) if isinstance(other, mint) else
            mint(self.x - other)
        )
    def __mul__(self, other):
        return (
            mint(self.x * other.x) if isinstance(other, mint) else
            mint(self.x * other)
        )
    def __floordiv__(self, other):
        return (
            mint(
                self.x * pow(other.x, MOD - 2, MOD)
            ) if isinstance(other, mint) else
            mint(self.x * pow(other, MOD - 2, MOD))
        )
    def __pow__(self, other):
        return (
            mint(pow(self.x, other.x, MOD)) if isinstance(other, mint) else
            mint(pow(self.x, other, MOD))
        )
    __radd__ = __add__
    def __rsub__(self, other):
        return (
            mint(other.x - self.x) if isinstance(other, mint) else
            mint(other - self.x)
        )
    __rmul__ = __mul__
    def __rfloordiv__(self, other):
        return (
            mint(
                other.x * pow(self.x, MOD - 2, MOD)
            ) if isinstance(other, mint) else
            mint(other * pow(self.x, MOD - 2, MOD))
        )
    def __rpow__(self, other):
        return (
            mint(pow(other.x, self.x, MOD)) if isinstance(other, mint) else
            mint(pow(other, self.x, MOD))
        )


n,s = map(int, input().split())
a = list(map(int, input().split()))
import copy
dp = [[0 for _ in range(s+1)] for _ in range(n+1)]
dp[0][0]=pow(2,n,MOD)
div=pow(2,MOD-2,MOD)
for i in range(n):
    for j in range(s+1):
        dp[i+1][j]=dp[i][j]
        if j-a[i]>=0:
            dp[i+1][j]+=dp[i][j-a[i]]*div
        dp[i+1][j]%=MOD
print(dp[n][s])