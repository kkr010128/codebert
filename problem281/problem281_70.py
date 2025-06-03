class Com:
    def __init__(self, MAX = 1000000, MOD = 1000000007):
        self.MAX = MAX
        self.MOD = MOD
        self._fac = [0]*MAX
        self._finv = [0]*MAX
        self._inv = [0]*MAX
        self._fac[0], self._fac[1] = 1, 1
        self._finv[0], self._finv[1] = 1, 1
        self._inv[1] = 1
        for i in range(2,self.MAX):
            self._fac[i] = self._fac[i - 1] * i % self.MOD
            self._inv[i] = self.MOD - self._inv[self.MOD%i] * (self.MOD // i) % self.MOD
            self._finv[i] = self._finv[i - 1] * self._inv[i] % self.MOD
    
    def com(self, n, k):
        if (n < k):
            return 0
        if (n < 0 or k < 0):
            return 0
        return self._fac[n] * (self._finv[k] * self._finv[n - k] % self.MOD) % self.MOD
a,b = list(map(int,input().split()))
if 2*a-b >= 0 and (2*a-b)%3 == 0 and a-2*((2*a-b)//3) >= 0:
    x = (2*a-b)//3
    y = a-2*x
    com = Com()
    print(com.com(x+y, x))
    exit()
a,b = b,a
if 2*a-b >= 0 and (2*a-b)%3 == 0 and a-2*((2*a-b)//3) >= 0:
    x = (2*a-b)//3
    y = a-2*x
    com = Com()
    print(com.com(x+y, x))
    exit()
print(0)