mod=998244353

class Combination:
    def __init__(self, N):
        self.fac = [1] * (N + 1)
        for i in range(1, N + 1):
            self.fac[i] = (self.fac[i - 1] * i) % mod
        self.invmod = [1] * (N + 1)
        self.invmod[N] = pow(self.fac[N], mod - 2, mod)
        for i in range(N, 0, -1):
            self.invmod[i - 1] = (self.invmod[i] * i) % mod
 
    def calc(self, n, k):  # nCk
        return self.fac[n] * self.invmod[k] % mod * self.invmod[n - k] % mod

N,M,K=map(int,input().split())

C=Combination(N)
ans=0
c=[1]*(N)
for i in range(1,N):
    c[i]=c[i-1]*(M-1)%mod
for i in range(K+1):
    tmp=M*c[N-i-1]*C.calc(N-1,N-i-1)%mod
    ans=(ans+tmp)%mod
print(ans)