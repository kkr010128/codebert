n,m,k = map(int,input().split())

def cmb(n, r, mod):#コンビネーションの高速計算　
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod
mod = 998244353 #出力の制限
N = n #Nの最大値
g1 = [0]*(N+1) #元テーブル(p(n,r))
g1[0] = g1[1] = 1
g2 = [0]*(N+1) #逆元テーブル
g2[0] = g2[1] = 1
inverse = [0]*(N+1) #逆元テーブル計算用テーブル
inverse[0],inverse[1] = 0,1
for i in range(2,N+1):
    g1[i] = (g1[i-1] * i) % mod
    inverse[i] = (-inverse[mod % i] * (mod//i)) % mod
    g2[i] = (g2[i-1] * inverse[i]) % mod

# i組　-> m * (n-1)Ci * (m-1)^(n-1-i)
ans = 0
for i in range(k+1):
    ans += m * cmb(n-1,i,mod) * pow(m-1,n-1-i,mod)
    ans %= mod
print(ans)