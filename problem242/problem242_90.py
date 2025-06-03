n,k = map(int,input().split())
a = list(map(int,input().split()))

def cmb(n, r, mod):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod

mod = 10**9+7 #出力の制限
N = 10**5+100
g1 = [1, 1] # 元テーブル
g2 = [1, 1] #逆元テーブル
inverse = [0, 1] #逆元テーブル計算用テーブル

for i in range( 2, N + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )
    
a.sort()

if k == 1:
    print(0)
else:
    ma,mi = 0,0
    for i in range(n-k+1):
        mi = (mi + (a[i] * cmb(n-1-i,k-1,mod))) % mod
        ma = (ma + (a[n-1-i] * cmb(n-1-i,k-1,mod))) % mod
        
    print((ma + mod - mi) % mod)