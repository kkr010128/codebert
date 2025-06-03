N,K=map(int, input().split())
AA=list(map(int, input().split()))
A=sorted(AA)
B=sorted(AA)[::-1]
mod=10**9+7

def cmb(n, r, mod):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod
mod = 10**9+7 #出力の制限
n = 10**5+1
g1 = [1, 1] # 元テーブル
g2 = [1, 1] #逆元テーブル
inverse = [0, 1] #逆元テーブル計算用テーブル

for i in range( 2, n+1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )

ans=0
for i in range(N-K+1):
  d=(A[K-1+i]%mod)*cmb(K-1+i,K-1,mod)
  e=(B[K-1+i]%mod)*cmb(K-1+i,K-1,mod)
  ans+=d%mod-e%mod
  ans%=mod
print(ans)
