SIZE=100001; MOD=10**9+7 #998244353 #ここを変更する

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


# coding: utf-8
# Your code here!
import sys
sys.setrecursionlimit(10**6)
readline = sys.stdin.readline
read = sys.stdin.read

n,k = [int(i) for i in readline().split()]
a = [int(i) for i in readline().split()]

a.sort()


ans = 0
for i in range(n):
    ans += a[i]*choose(i,k-1)
    ans -= a[i]*choose(n-i-1,k-1)
    ans %= MOD

print(ans)


