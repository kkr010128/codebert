import sys
sys.setrecursionlimit(2147483647)

n,k=map(int,input().split())
#n個の中からk個選んだ時の最大と最小

a=list(map(int,input().split()))
"""
seta=set([])
dic={}

for v in a:
    if v in seta:
        dic[v]+=1
    else:
        dic[v]=1
        seta.add(v)

a=list(seta)
"""

a.sort()

def cmb(n, r, p):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n-r] % p
p = 10**9+7 #割る数
N = 10 ** 6  # N は必要分だけ用意する
fact = [1, 1]  # fact[n] = (n! mod p)
factinv = [1, 1]  # factinv[n] = ((n!)^(-1) mod p)
inv = [0, 1]  # factinv 計算用
for i in range(2, N + 1):
    fact.append((fact[-1] * i) % p)
    inv.append((-inv[p % i] * (p // i)) % p)
    factinv.append((factinv[-1] * inv[-1]) % p)


result=0
for i,v in enumerate(a):
    if i>=k-1:
        result+=v*cmb(i, k-1, p)
    
    if k-1<=n-i-1:
        result-=v*cmb(n-i-1, k-1, p)

print(result%p)
        


