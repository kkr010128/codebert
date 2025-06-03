K = int(input())
S = input()
X = len(S)
mod = 10**9+7

def cmb(n, r, mod):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod

mod = 10**9+7 #出力の制限
N = 2*10**6
g1 = [1, 1] # 元テーブル
g2 = [1, 1] #逆元テーブル
inverse = [0, 1] #逆元テーブル計算用テーブル

for i in range( 2, N + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )

def power(n, r, mod):
    if r == 0: return 1
    if r%2 == 0:
        return power(n*n % mod, r//2, mod) % mod
    if r%2 == 1:
        return n * power(n, r-1, mod) % mod


A = 0
B = K
temp = cmb(A+X-1,X-1,mod)*power(25,A,mod)
temp %= mod
temp *= power(26,B,mod)
temp %= mod

ans = temp

for i in range(X+1,K+X+1):

    temp *= 25
    temp %= mod
    
    temp *= pow(26, mod-2, mod)
    temp %= mod
    
    temp *= i-1
    temp %= mod
    
    temp *= pow(i-X, mod-2, mod)
    temp %= mod    

    ans += temp
    ans %= mod

print(ans)