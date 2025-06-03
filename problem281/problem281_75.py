X, Y = map(int, input().split())

def cmb(n, r, mod):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod

mod = 10**9+7 
N = 10**6
g1 = [1, 1] # 元テーブル
g2 = [1, 1] #逆元テーブル
inverse = [0, 1] #逆元テーブル計算用テーブル

for i in range( 2, N + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )

step1_cnt = 0
step2_cnt = 0
if Y == X:
    if Y % 3 == 0:
        step1_cnt = step2_cnt = Y//3
        print(cmb(step1_cnt+step2_cnt,step1_cnt,mod))
    else:
        print(0)
if Y > X:
    step1_cnt = Y-X
    Y = Y - step1_cnt*2
    X = X - step1_cnt
    if Y % 3 == 0:
        step1_cnt += Y//3
        step2_cnt += Y//3
        print(cmb(step1_cnt+step2_cnt,step1_cnt,mod))
    else:
        print(0)

if X > Y:
    step2_cnt = X - Y
    Y = Y - step2_cnt
    X = X - step2_cnt*2
    if Y % 3 == 0:
        step1_cnt += Y//3
        step2_cnt += Y//3
        print(cmb(step1_cnt+step2_cnt,step1_cnt,mod))
    else:
        print(0)
