import sys
input = sys.stdin.readline

MAX = 2*10**6+100
MOD = 10**9+7
fact = [0]*MAX #fact[i]: i!
inv = [0]*MAX #inv[i]: iの逆元
finv = [0]*MAX #finv[i]: i!の逆元
fact[0] = 1
fact[1] = 1
finv[0] = 1
finv[1] = 1
inv[1] = 1
    
for i in range(2, MAX):
    fact[i] = fact[i-1]*i%MOD
    inv[i] = MOD-inv[MOD%i]*(MOD//i)%MOD
    finv[i] = finv[i-1]*inv[i]%MOD

def C(n, r):
    if n<r:
        return 0
    if n<0 or r<0:
        return 0
    return fact[n]*(finv[r]*finv[n-r]%MOD)%MOD
    
K = int(input())
S = input()[:-1]
L = len(S)
ans = 0

for i in range(L, L+K+1):
    ans += C(i-1, L-1)*pow(25, i-L, MOD)*pow(26, L+K-i, MOD)
    ans %= MOD

print(ans)