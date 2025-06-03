n,k = map(int,input().split())
a_ls = list(map(int, input().split()))
a_ls.sort()
class Combination():
    def __init__(self, n, mod=10**9+7):
        self.mod = mod
        self.fac = [1]*(n+1)
        for i in range(1,n+1):
            self.fac[i] = self.fac[i-1] * i % self.mod
        self.invfac = [1]*(n+1)
        self.invfac[n] = pow(self.fac[n], self.mod - 2, self.mod)
        for i in range(n-1, 0, -1):
            self.invfac[i] = self.invfac[i+1] * (i+1) % self.mod
 
    def combination(self, n, r):
        if n < r:
            return 0
        return self.fac[n] * self.invfac[r] % self.mod * self.invfac[n-r] % self.mod
 
    def permutation(self, n, r):
        return self.factorial(n) * self.invfactorial(n-r) % self.mod
 
    def factorial(self, i):
        return self.fac[i]
 
    def invfactorial(self, i):
        return self.invfac[i]
c = Combination(n)

ans = 0
for i in range(n-1,-1,-1):
    time_min = c.combination(n-i-1,k-1)
    time_max = c.combination(i,k-1)
    ans += time_max * a_ls[i]
    ans -= time_min * a_ls[i]
    '''
    print(time_min)
    print(i,k)
    print(time_max)
    print(ans)
    '''
    ans %= 10**9+7
print(ans)