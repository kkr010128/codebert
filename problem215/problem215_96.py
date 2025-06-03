import sys
sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))
SIZE=4*10**5+1; MOD=10**9+7 #998244353 #ここを変更する
 
SIZE += 1
inv = [0]*SIZE  # inv[j] = j^{-1} mod MOD
fac = [0]*SIZE  # fac[j] = j! mod MOD
finv = [0]*SIZE # finv[j] = (j!)^{-1} mod MOD
inv[1] = 1
fac[0] = fac[1] = 1
finv[0] = finv[1] = 1
for i in range(2,SIZE):
    inv[i] = MOD - (MOD//i)*inv[MOD%i]%MOD
    fac[i] = fac[i-1]*i%MOD
    finv[i]= finv[i-1]*inv[i]%MOD
 
def choose(n,r): # nCk mod MOD の計算
    if 0 <= r <= n:
        return (fac[n]*finv[r]%MOD)*finv[n-r]%MOD
    else:
        return 0
def resolve():
    n, k = lr()
    ans = choose(2*n-1, n)
    if n-1 > k:
        for i in range(1, n-k):
            ans -= choose(n, i)*choose(n-1, n-i)
            ans %= MOD
    print(ans)
resolve()