
import numpy as np

class Combination : 
    def __init__ (self, N=10**6, mod=10**9+7) :
        self.mod = mod
        self.fact = [1, 1]
        self.factinv = [1, 1]
        self.inv = [0, 1]
        for i in range(2, N+1) :
            self.fact.append( (self.fact[-1]  * i) % mod )
            self.inv .append( (-self.inv[mod%i] * (mod//i) ) % mod )
            self.factinv.append( (self.factinv[-1] * self.inv[-1]) % mod )

    def nCr(self, n, r) :
        if ( r < 0 ) or ( n < r ) : return 0
        r = min(r, n-r)
        return self.fact[n]*self.factinv[r]*self.factinv[n-r] % self.mod

    def nPr(self, n, r) :
        if ( r < 0 ) or ( n < r ) : return 0
        return self.fact[n]*self.factinv[n-r] % self.mod


n, k = map(int, input().split())

mod = 10**9+7
comb = Combination(2*10**5+100)
ans = 0
for m in range(min(n+1,k+1)) :
    ans = ans%mod + (comb.nCr(n,m) * comb.nCr(n-1, n-m-1))%mod
print(ans%mod)
