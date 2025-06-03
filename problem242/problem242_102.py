""" 逆元を利用し、nCrを高速で求めるクラス """
class Cmb:
    def __init__(self, N=10**5, mod=10**9+7):
        self.fact = [1,1]
        self.fact_inv = [1,1]
        self.inv = [0,1]
        
        """ 階乗を保存する配列を作成 """
        for i in range(2, N+1):
            self.fact.append((self.fact[-1]*i) % mod)
            self.inv.append((-self.inv[mod%i] * (mod//i))%mod)
            self.fact_inv.append((self.fact_inv[-1]*self.inv[i])%mod)
    
    """ 関数として使えるように、callで定義 """
    def __call__(self, n, r, mod=10**9+7):
        if (r<0) or (n<r):
            return 0
        r = min(r, n-r)
        return self.fact[n] * self.fact_inv[r] * self.fact_inv[n-r] % mod

N,K = map(int,input().split())
A = list(map(int,input().split()))
mod=10**9+7
A.sort()
A_rev = A[::-1]
f_max, f_min = 0, 0
cmb = Cmb(mod=mod)
for i, num in enumerate(A):
    f_max += num*cmb(i, K-1) if i >= K-1 else 0
for i, num in enumerate(A_rev):
    f_min += num*cmb(i, K-1) if i >= K-1 else 0
print((f_max - f_min)%mod)