k=int(input())
s=input()

mod=10**9+7

import sys
sys.setrecursionlimit(10**9)

def cmb(n, r, p):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n-r] % p
p = mod #割る数
N = 2*(10 ** 6)  # N は必要分だけ用意する
fact = [1, 1]  # fact[n] = (n! mod p)
factinv = [1, 1]  # factinv[n] = ((n!)^(-1) mod p)
inv = [0, 1]  # factinv 計算用
for i in range(2, N + 1):
    fact.append((fact[-1] * i) % p)
    inv.append((-inv[p % i] * (p // i)) % p)
    factinv.append((factinv[-1] * inv[-1]) % p)

ans=0

for i in range(k+1):
    ans = (ans+cmb(i+len(s)-1,i,mod)*pow(26,k-i,mod)*pow(25,i,mod)) % mod

    #print(end,len(s)+k-end,ans,cmb(end,len(s),mod),pow(25,end-len(s),mod),pow(26,len(s)+k-end,mod))

print(ans%mod)



