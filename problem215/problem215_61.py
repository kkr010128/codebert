

n,k = map(int,input().split())


class Combination(): # nCr mod MOD など
    """
    O(n+log(mod))の前計算を1回行うことで，O(1)でnCr mod mを求められる
    n_max = 10**6のとき前処理は約950ms (PyPyなら約340ms, 10**7で約1800ms)
    使用例：
    C = Combination(10**6)
    print(C.combi_mod(5, 3))  # 10
    """
    def __init__(self, n_max, mod=10**9+7): # O(n+log(mod))
        self.mod = mod
        self.fac, self.facinv = self.prepare(n_max)
        #self.modinv = self.make_modinv_list(n_max) ##なくても問題ないので、必要な時のみ使う
        
    def prepare(self,n): # O(n+log(mod))
        # 前処理(コンストラクタで自動的に実行)
        # 1! ~ n! の計算
        factorials = [1]  # 0!の分
        for m in range(1, n+1):
            factorials.append(factorials[m-1]*m%self.mod)
        # n!^-1 ~ 1!^-1 の計算
        invs = [1] * (n+1)
        invs[n] = pow(factorials[n], self.mod-2, self.mod)
        for m in range(n, 1, -1):
            invs[m-1] = invs[m]*m%self.mod
        return factorials, invs # list
    
    def make_modinv_list(self, n): # O(n)
        # 0からnまでのmod逆元のリストを返す O(n)
        modinv = [0] * (n+1)
        modinv[1] = 1
        for i in range(2, n+1):
            # 整数aのMを法とした時の逆元a^-1は、(0<=a<=M-1)
            # a == qM+rであるとき(qは商,rは余り)、
            # a^-1 == -qr^-1 % M で与えられる。
            modinv[i] = (self.mod - self.mod//i)*modinv[self.mod%i]  % self.mod
        return modinv

    def perm_mod(self,n,r): # nPr % self.mod
        if n < r:
            return 0
        if (n < 0 or r < 0):
            return 0
        return (self.fac[n] * self.facinv[n-r]) % self.mod

    def combi_mod(self,n,r): # nCr % self.mod
        if n < r:
            return 0
        if (n < 0 or r < 0):
            return 0
        return (((self.fac[n] * self.facinv[r]) % self.mod) * self.facinv[n-r]) % self.mod

    def repeated_permutation(self,n,deno): # 重複順列
        # n!/(deno[0]!*deno[1]!*...*deno[len(deno)-1]) % MOD
        ## n:int(分子),deno:分母のlist
        if n < max(deno):
            return 0
        if (n < 0 or min(deno) < 0):
            return 0
        D = 1
        for i in range(len(deno)):
            D = D*self.facinv[deno[i]] % self.mod
        return self.fac*D % self.mod # int ## == n!/(deno[0]!*deno[1]!*...*deno[len(deno)-1]) % MOD
    
    def H(self,n,r): # 重複組合せ nHr % self.mod
        now_n = len(self.fac)
        if now_n < n+r-1: # もしself.facの長さが足りなかったら追加
            for i in range(now_n+1, n+r-1+1):
                self.fac.append(self.fac[i-1]*i%self.mod)
        return self.combi_mod(n+r-1,r)


mod = 10**9+7
C = Combination(n,mod)
ans = 0
for i in range(min(k+1,n+1)):
    ans += C.combi_mod(n,i)*C.H(n-i,i)
    ans %= mod
print(ans)

