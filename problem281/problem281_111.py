def pre_combi1(n, p):
    fact = [1]*(n+1)  # fact[n] = (n! mod p)
    factinv = [1]*(n+1)  # factinv[n] = ((n!)^(-1) mod p)
    inv = [0]*(n+1)  # factinv 計算用
    inv[1] = 1
    # 前処理
    for i in range(2, n + 1):
        fact[i]= fact[i-1] * i % p
        inv[i]= -inv[p % i] * (p // i) % p
        factinv[i]= factinv[i-1] * inv[i] % p
    return fact, factinv

def combi1(n, r, p, fact, factinv):
    if r < 0 or n < r:
        return 0
    r = min(r, n-r)
    return fact[n] * factinv[r] * factinv[n-r] % p

import sys
x,y=map(int,input().split())
if (x+y)%3 > 0:
  print(0)
  sys.exit()
n=(x+y)//3
r=x-n
f,inv=pre_combi1(n,1000000007)
print(combi1(n,r,1000000007,f,inv))